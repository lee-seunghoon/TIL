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
naver_client_id = 'naver_application_id'
naver_client_secret = 'naver_application_pw'


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

    fs.close()
