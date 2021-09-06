import re
import json
import math
import datetime
import requests
import urllib.request
import urllib.error

# 파싱하는 라이브러리
import urllib.parse

from bs4 import BeautifulSoup

# Naver API 애플케이션 인가 정보
naver_client_id = 'cGLyzyPcu9B2t_Oj0DhX'
naver_client_secret = 'PKxpmEmFe4'


def get_blog_count(query, display):

    # 우리가 사용할 쿼리 질문을 인코딩하는 작업
    encode_query = urllib.parse.quote(query)  # ==> '%EB%8C%80%EC%84%A0' 이런 요상한 인코딩 결과가 나온다.
    search_url = "https://openapi.naver.com/v1/search/blog?query=" + encode_query
    request = urllib.request.Request(search_url)  # 위 search_url 형태로 request 요청한다.

    # 그냥하면 네이버의 API로부터 거부 당해서 인가 과정이 필요하다.
    request.add_header('X-Naver-Client-id', naver_client_id)
    request.add_header('X-Naver-Client-secret', naver_client_secret)

    # request로부터 받아온 response 정의
    response = urllib.request.urlopen(request)  # <http.client.HTTPResponse at 0x151bdcfd148> 객체 부여

    # 정상적으로 받아왔는지 response code 확인
    response_code = response.getcode()

    # 200이 정상이라서 200으로 잘 받아 왔다면
    if response_code is 200:

        response_body = response.read()
        # json 형식으로 넘겨준다
        # "lastBuildDate": "Sat, 04 Sep 2021 22:33:31 +0900",\n"total": 1711543,\n"start": 1,\n"display": 10 ...
        # 이런식으로 정보를 담고 있고, 내용은 위에서 urllib.parse()로 인코딩한 것처럼 된 문자열을 출력해준다.
        # response_body.decode('utf-8') utf-8로 디코드 해주면 한글로 바뀐다.

        # json으로 받은 response_body를 python 의 dict 형식으로 전환
        # json 형식의 데이터를 dict 형식의 데이터로 전환하는 방법 == json.loads(json데이터)
        # 그런데 그 데이터가 byte 형식으로 인코딩 돼 있으면, 꼭 디코딩을 하고 가져와야 정상적으로 가져올 수 있다.
        response_body_dict = json.loads(response_body.decode('utf-8'))

        print('Last build date :', str(response_body_dict['lastBuildDate']))
        print('Total :', str(response_body_dict['total']))  # 전체 게시글 개수
        print('Start :', str(response_body_dict['start']))
        print('Display :', str(response_body_dict['display']))

        # 만약 검색된 결과가 없을 경우
        if response_body_dict['total'] == 0:
            blog_count = 0
            print('Blog_Count : 0(없습니다)',)
        else:
            # display 개수 만큼 1페이지에 보여주는데, 총 블로그 내용을 가져올 페이지를 제한 하기 위해서
            # 전체 게시글에서 display만큼 나눈 값을 가져온다.
            # math.ceil() == 나머지가 있으면 몫에서 무조건 올림
            blog_total = math.ceil(response_body_dict['total'] / int(display))

            # 전체 블로그 페이지를 가져오는 수를 1000으로 제한하기 위해
            if blog_total >= 1000:
                blog_count = 1000
            else:
                blog_count = blog_total

            print('Blog_Count :', str(blog_count))
            print('Blog_Total :', str(blog_total))

    return blog_count

# 전체 블로그 포스팅 글을 긁어오는 함수
def get_blog_post(query, display, start_idx, sort):
    # 전역 변수 세팅
    global no, fs

    encode_query = urllib.parse.quote(query)

    # 추가 적으로 display, start, sort 변수를 입력한다.
    search_url = 'https://openapi.naver.com/v1/search/blog?query=' + encode_query \
                 + '&display=' + str(display) + '&start=' + str(start_idx) + '&sort=' + str(sort) 
    request = urllib.request.Request(search_url)

    request.add_header('X-Naver-Client-Id', naver_client_id)
    request.add_header('X-Naver-Client-Secret', naver_client_secret)

    response = urllib.request.urlopen(request)
    response_code = response.getcode()

    if response_code is 200 :
        response_body = response.read()
        response_body_dict = json.loads(response_body.decode('utf-8'))
        for item_idx in range(0, len(response_body_dict['items'])):
            try:
                remove_html_tag = re.compile('<.*?>')  # html tag가 들어가 있어서 특수기호 지운다
                title = re.sub(remove_html_tag, '', response_body_dict['items'][item_idx]['title'])
                # 링크를 가져오는데, 쓸모 없는 amp; 이런 게 포함 돼 있는 경우도 있어서 지운다.
                link = response_body_dict['items'][item_idx]['title'].replace('amp;', '')
                # description도 쓸모없는 특수기호 지운다
                description = re.sub(remove_html_tag, '', response_body_dict['items'][item_idx]['description'])
                # 블로거 이름
                blogger_name = response_body_dict['items'][item_idx]['bloggername']
                # 블로거 링크 == 호스트 주소가 아니라, 블로그의 주소
                blogger_link = response_body_dict['items'][item_idx]['bloggerlink']
                # 포스팅 날짜
                post_date = response_body_dict['items'][item_idx]['postdate']

                no += 1
                print('-'*20)
                print('#' + str(no))
                print('Title :', title)
                print('Link :', link)
                print('Description :', description)
                print('Blogger Name :', blogger_name)
                print('Blogger link :', blogger_link)
                print('Blog Date :', post_date)

                # 위에서 가져온 link를 활용해서 웹스크래핑 하기 위해 bs4 객체 생성
                post_code = requests.get(link)
                post_text = post_code.text
                post_soup = BeautifulSoup(post_text, 'lxml')

                # 하지만 네이버 블로그는 드래그, 우클릭 복사를 막기 위해 설정이 하나 더 걸려 있다.
                # iframe 이란 element로 접근해서 진짜 블로그 url을 가져와야 한다.
                for mainFrame in post_soup.select('iframe#mainFrame'):
                    # 진짜 블로그 url
                    blog_post_url = 'http://blog.naver.com'+ mainFrame.get('src')
                    blog_post_code = requests.get(blog_post_url)
                    blog_post_text = blog_post_code.text
                    blog_post_soup = BeautifulSoup(blog_post_text, 'lxml')

                    # 블로그 내용 중에서 실제 내용만 가져올건데 그 내용은
                    # div tag에서 postViewArea 라는 tag에 있다.
                    for blog_post_content in blog_post_soup.select('div#postViewArea'):
                        blog_post_content_text = blog_post_content.get_text()
                        blog_post_full_contents = str(blog_post_content_text)
                        blog_post_full_contents = blog_post_full_contents.replace('\n\n', '\n')

                        # 파일에 내용을 저장하자
                        fs.write(blog_post_full_contents + '\n')
                        fs.write('-'*20)
            except:
                item_idx += 1



if __name__ == '__main__':
    no = 0          # 몇개의 포스트를 저장하였는지 세기 위한 index
    query = '대선'  # 검색을 원하는 문자열로서 UTF-8로 인코딩 진행
    display = 10    # 검색 결과 출력 건수 지정, 10(기본값), 100(최대)
    start = 1       # 검색 시작 위치로 최대 1000까지 가능
    sort = 'date'   # 정렬 옵션 : sim(유사도순, 기본값), date(날짜순)

    # 블로그 컨텐츠를 한글로 저장하기 위해 encoding = 'utf-8' 로 지정
    fs = open(query + '.txt', 'a', encoding='utf-8')  # 왜 'w'가 아니라 'a'일까?
                                                      # append 하는 목적. 파일이 없으면 일단 만들고
                                                      # 새로운 내용을 계속 추가하는 파일 형식

    blog_count = get_blog_count(query, display)

    # 블로그 포스팅 가져오자
    for start_idx in range(start, blog_count + 1, display):
        get_blog_post(query, display, start_idx, sort)

    fs.close()
