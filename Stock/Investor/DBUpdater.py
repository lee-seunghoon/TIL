import pymysql
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup as bs
import requests
import json
import calendar
import time
from threading import Timer


# DBUpdater class는 객체가 생성될 때, 마리아디비에 접속하고, 소멸될 때 접속을 해제한다.
class DBUpdater:
    def __init__(self):
        ''' 생성자 : MariaDB 연결 및 종목코드 딕셔너리 생성'''
        self.conn = pymysql.connect(host='localhost', user='root', password='tmdgns001!',
                                    db='INVESTAR', charset='utf8')

        # 이미 존재하는 DB 테이블에 `CREATE TABLE` 구문을 사용하면 오류가 발생하면서 프로그램 종료!
        # 그래서 IF NOT EXIST 구문을 추가하여 경고 메시지만 표시하고 프로그램은 계속 실행될 수 있도록 설정!
        with self.conn.cursor() as curs:
            sql = """
            CREATE TABLE IF NOT EXISTS company_info (
                code VARCHAR(20),
                company VARCHAR(20),
                last_update DATE,
                PRIMARY KEY (code)
            );
            """
            curs.execute(sql)
            sql = """
            CREATE TABLE IF NOT EXISTS daily_price (
                code VARCHAR(20),
                date DATE,
                open BIGINT(20),
                high BIGINT(20),
                low BIGINT(20),
                close BIGINT(20),
                diff BIGINT(20),
                volume BIGINT(20),
                PRIMARY KEY (code, date)
            );
            """
            curs.execute(sql)
        self.conn.commit()
        self.codes = dict()

    def __del__(self):
        ''' 소멸자: MariaDB 연결 해제'''
        self.conn.close()

    def read_krx_code(self):
        """ KRX로부터 상장법인목록 파일을 읽어와서 데이터프레임으로 반환"""
        url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=' \
              'download&searchType=13'
        krx = pd.read_html(url, header=0)[0]
        krx = krx[['종목코드', '회사명']]
        krx = krx.rename(columns={'종목코드': 'code', '회사명': 'company'})
        krx.code = krx.code.map('{:06d}'.format)
        return krx

    def update_comp_info(self):
        """종목코드를 company_info 테이블에 업데이트한 후 딕셔너리에 저장"""
        sql = "SELECT * FROM company_info"
        df = pd.read_sql(sql, self.conn)  # 'company_info' 테이블을 read_sql() 함수로 읽는다.

        # 위에서 읽은 df 이용해서 종목코드와 회사명으로 codes 딕셔너리를 만든다.
        for idx in range(len(df)):
            self.codes[df['code'].values[idx]] = df['company'].values[idx]

        with self.conn.cursor() as curs:
            # DB에서 가장 최근 업데이트 날짜 가져온다.
            sql = "SELECT max(last_update) FROM company_info"
            curs.execute(sql)
            rs = curs.fetchone()
            today = datetime.today().strftime('%Y-%m-%d')

            # 위에서 객체 설정한 rs가 없거나, 오늘보다 오래된 경우 업데이트!
            if rs[0] == None or rs[0].strftime('%Y-%m-%d') < today:
                krx = self.read_krx_code()  # krx 상장기업 목록 파일을 읽어서 krx 데이터프레임 저장
                for idx in range(len(krx)):
                    code = krx.code.values[idx]
                    company = krx.company.values[idx]
                    # 일반적으로 테이블 데이터 행 삽입하는데 INSER INTO 구문 사용 But 이미 있으면 오류
                    # 마리아디비에서 제공해주는 `REPLACE INTO` 사용 ==> 동일한 data 존재 하면 오류 X update 진행
                    sql = f"REPLACE INTO company_info (code, company, last_update) VALUES ('{code}', '{company}', '{today}')"
                    curs.execute(sql)

                    # codes 딕셔너리에 '키-값'으로 종목코드와 회사명을 추가
                    self.codes[code] = company
                    tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
                    print(f"[{tmnow}] {idx:04d} REPLACE INTO company_info VALUES ('{code}', '{company}', '{today}')")
                self.conn.commit()
                print()

    def read_naver(self, code, company, pages_to_fetch):
        """ 네이버 금융에서 주식 시세를 읽어서 데이터프레임으로 반환"""
        try:
            url = f"https://finance.naver.com/item/sise_day.nhn?code={code}"
            html = bs(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text, 'lxml')
            pgrr = html.find('td', class_='pgRR')
            if pgrr is None :
                return None
            s = str(pgrr.a['href']).split('=')
            last_page_num = s[-1]  # 네이버 증권 일별 시세에서 맨 마지막 페이지 번호 구하기
            df = pd.DataFrame()

            # 설정 파일에 설정된 페이지 수(pages_to_fetch)와 last_page_num 비교하여 작은 것 선택
            pages = min(int(last_page_num), pages_to_fetch)
            for page in range(1, pages+1):
                pg_url = '{}&page={}'.format(url, page)
                df = df.append(pd.read_html(requests.get(pg_url, headers={'User-agent': 'Mozilla/5.0'}).text)[0])
                tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
                print('[{}] {} ({}) : {:04d}/{:04d} pages are downloading...'.format(tmnow, company, code, page, pages), end="\r")

            df = df.rename(columns={'날짜':'date', '종가':'close', '전일비':'diff', '시가':'open', '고가':'high',
                                    '저가':'low', '거래량':'volume'})
            df['date'] = df['date'].replace('.', '-')
            df = df.dropna()

            # 마리아디비에서 BIGINT형으로 지정한 칼럼들의 데이터 형을 int형으로 변경!!
            df[['close', 'diff', 'open', 'high', 'low', 'volume']] = \
                df[['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int)
            df = df[['date', 'open', 'high', 'low', 'close', 'diff', 'volume']]
        except Exception as e :
            print('Exception occured :', str(e))
            return None
        return df

    def replace_into_db(self, df, num, code, company):
        """네이버 금융에서 읽어온 주식 시세를 DB에 REPLACE"""
        with self.conn.cursor() as curs :
            for r in df.itertuples(): # 인수로 넘겨 받은 데이터프레임을 튜플로 순회처리!
                sql = f"REPLACE INTO daily_price VALUES ('{code}'," \
                      f"'{r.date}', {r.open}, {r.high}, {r.low}, {r.close}, {r.diff}, {r.volume})"
                curs.execute(sql)
            self.conn.commit()
            print('[{}] #{:04d} {} ({}) : {} rows > REPLACE INTO daily_price [OK]'.format(
                datetime.now().strftime('%Y-%m-%d %H:%M'), num+1, company, code, len(df)
            ))

    def update_daily_price(self, pages_to_fetch):
        """KRS 상장법인의 주식 시세를 네이버로부터 읽어서 DB에 업데이트"""
        for idx, code in enumerate(self.codes):
            # 종목코드에 대한 일별 시세 데이터 프레임 가져온다
            df = self.read_naver(code, self.codes[code], pages_to_fetch)
            if df is None:
                continue
            # 일별 시세 데이퍼 프레임 구하면 DB에 저장한다.
            self.replace_into_db(df, idx, code, self.codes[code])

    def execute_daily(self):
        """실행 즉시 및 매일 오후 다섯시에 daily_price 테이블 업데이트"""
        self.update_comp_info() # 상장 법인 목록을 update 한다.
        try:
            # DBUpdater.py가 있는 디렉터리에서 config.json 파일을 읽기 모드로 연다.
            with open('config.json', 'r') as in_file:
                config = json.load(in_file)
                # 파일이 있다면 pages_to_fetch 값을 읽어서 사용한다.
                pages_to_fetch = config['pages_to_fetch']
        except FileNotFoundError: # 'config.json' 파일이 없을 경우!
            # 최초 실행 시 프로그램에서 사용할 pages_to_fetch값을 100으로 설정
            # ('config.json' 파일에 pages_to_fetch값을 1로 저장해서 이후부터는 1페이지씩 읽기)
            with open('config.json', 'w') as out_file:
                pages_to_fetch = 100
                config = {'pages_to_fetch':1}
                json.dump(config, out_file)
        self.update_daily_price(pages_to_fetch)

        tmnow = datetime.now()
        # 이번 달 마지막 날을 구해서 다음 날 오후 5시를 계산하는 데 사용
        lastday = calendar.monthrange(tmnow.year, tmnow.month)[1]

        if tmnow.month == 12 and tmnow.day == lastday:
            tmnext = tmnow.replace(year=tmnow.year+1, month=1, day=1, hour=18, minute=0, second=0)
        elif tmnow.day == lastday:
            tmnext = tmnow.replace(month=tmnow.month+1, day=1, hour=18, minute=0, second=0)
        else:
            tmnext = tmnow.replace(day=tmnow.day+1, hour=18, minute=0, second=0)
        tmdiff = tmnext - tmnow
        secs = tmdiff.seconds

        # 다음 날 오후 5시에 execute_daily() 메서드 실행하는 타이머(Timer) 객체 생성
        t = Timer(secs, self.execute_daily)
        print("Waiting for next update ({}) ... ".format(tmnext.strftime('%Y-%m-%d %H:%M')))
        t.start()


if __name__ == '__main__':
    dbu = DBUpdater()
    dbu.execute_daily()
