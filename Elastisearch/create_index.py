"""
config 파일 활용하여 엘라스틱서치 서버 내 index 생성하는 메서드
"""

from json import load
from argparse import ArgumentParser
from elasticsearch import Elasticsearch

es_url = "http://localhost:9200"    # 로컬에 설치된 엘라스틱서치 서버 주소
es=Elasticsearch(es_url)


def create_index(index: str, config: str):
    """
    인덱스 생성 기능
    index : 인덱스 이름
    config : 인덱스 생성을 위한 환경설정 json 파일 경로
    """
    try:
        with open(config) as file:
            config = load(file)
        es.indices.create(index=index, body=config)
        print("[INFO] index " + index + " has been created!")
    except Exception as e:
        print(e)
        print("[WARNING] some exception has occurred!")


def delete_index(index):
    """
    인덱스 삭제 기능
    index : 삭제 할 인덱스 이름
    """
    try:
        es.indices.delete(index=index)
        print("[INFO] index " + index + " has been deleted!")
    except Exception as e:
        print(e)
        print("[WARNING] some exception has occurred!")


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument('--index', required=True, help='name of the ES index')
    parser.add_argument('--config', required=True, help='path to the ES mapping config')
    parser.add_argument('--delete', required=False, help='Delete?')
    args = parser.parse_args()
    if args.delete : 
        delete_index(args.index)
    create_index(args.index, args.config)
