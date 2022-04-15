# 개요

- Dataproc은 빠르고 사용하기 쉬운 완전 관리형 클라우드 서비스로서 [Apache Spark](http://spark.apache.org/) 및 [Apache Hadoop](http://hadoop.apache.org/) 클러스터를 더 간단하고 비용 효율적인 방식으로 실행
- Cloud Dataproc 클러스터를 신속하게 만들고 언제든지 크기를 조정할 수 있으므로 클러스터보다 많은 데이터 파이프라인이 생길 염려가 없습니다.
- gcloud를 사용하여 Google Cloud Dataproc 클러스터를 만들고, 클러스터에서 간단한 [Apache Spark](http://spark.apache.org/) 작업을 실행한 다음, 클러스터의 작업자 수를 수정하는 방법을 살벼봅니다.



## 클러스터 생성

- 리전 설정

  ```shell
  gcloud config set dataproc/region us-central1
  ```

- 기본 cloud dataproc 설정으로 `example-cluster` 라는 이름의 클러스터 생성

  ```shell
  gcloud dataproc clusters create example-cluster --worker-boot-disk-size 500
  ```

  - 클러스터 영역 확인하라고 하면 Y 입력 & 클러스터는 몇 분 동안 빌드됩니다.

  ```shell
  # 출력화면
  Waiting for cluster creation operation...done.
  Created [... example-cluster]
  ```

  

## 작업 제출

- 대략적인 pi 값을 계산하는 샘플 Spart 작업을 제출하기 위해 다음 명령을 실행

  ```shell
  gcloud dataproc jobs submit spark --cluster example-cluster \
  --class org.apache.spark.examples.SparkPi \
  --jars file:///usr/lib/spark/examples/jars/spark-examples.jar -- 1000
  ```

  - `example-cluster` 클러스터에서 spark 작업을 실행하고자 함
  - 작업의 pi를 계산하는 애플리케이션에 대한 기본 메소드가 포함된 class
  - 작업의 코드가 포함된 jar 파일의 위치
  - 작업에 전달할 매개변수(이 경우 작업 개수인 1000)



## 클러스터 업데이트

- 클러스터의 작업자 수를 4로 변경하려면 다음 명령어를 실행

  ```shell
  gcloud dataproc clusters update example-cluster --num-workers 4
  ```

  

- 클러스터의 업데이트된 세부정보는 명령의 출력에 표시

  ```shell
  Waiting on operation [projects/qwiklabs-gcp-02-71d08ed53d3b/regions/us-central1/operations/ae13271d-a1ed-30c4-bfe1-c6cd16e37e67].
  Waiting for cluster update operation...done.     
  Updated [https://dataproc.googleapis.com/v1/projects/qwiklabs-gcp-02-71d08ed53d3b/regions/us-central1/clusters/example-cluster].
  ```

  

- 동일한 명령어를 사용하여 작업자 노드의 수 또한 줄일 수 있다.

  ```shell
  gcloud dataproc clusters update example-cluster --num-workers 2
  ```



- 이제 Dataproc 클러스터를 만들고 Google cloud의 `gcloud` 명령줄에서 작업자 수를 조정할 수  있다.