# elasticsearch image 불러올 링크 경로
FROM docker.elastic.co/elasticsearch/elasticsearch:7.17.7

# 현재 경로에서 특정 디렉토리 안에 있는 파일을 docker image 디렉토리 안으로 복사
COPY analysis/test.txt config/analysis/synonym.txt

# analysis-nori plugin 설치
RUN bin/elasticsearch-plugin install analysis-nori