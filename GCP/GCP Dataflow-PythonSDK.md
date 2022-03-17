# 개요

- Python 개발 환경을 설정
- Python용 Cloud Dataflow SDK를 가져오고
- Google Cloud Platform Console을 사용하여 예시 파이프라인을 실행





# 실습



## 1. 버킷 생성

- region : us-central1



## 2. pip 및 Cloud Dataflow SDK 설치

1. Python용 Cloud Dataflow SDK에는 Python 버전 3.7이 필요

   - 올바른 버전으로 프로세스를 실행하고 있는지 확인하려면 `Python3.7` Docker 이미지를 실행

   - 이 명령은 최신 안정 버전의 Python 3.7이 포함된 Docker 컨테이너를 가져온 다음 컨테이너 내에서 다음 명령을 실행할 수 있도록 명령 셸을 엽니다.

     ```shell
     docker run -it -e DEVSHELL_PROJECT_ID=$DEVSHELL_PROJECT_ID python:3.7 /bin/bash
     ```

2. 가상 환경에서 다음 명령어를 실행하여 Python용 Apache Beam SDK의 최신 버전을 설치합니다.

   - 종속성 항목과 관련된 몇 가지 경고가 표시되지만 이 실습에서는 무시해도 됩니다.

   ```shell
   pip install apache-beam[gcp]
   ```

3. 다음 명령어를 실행하여 `wordcount.py` 예시를 로컬에서 실행합니다.

   - `google-cloud-dataflow`를 설치했지만 `wordcount`를 `apache_beam`으로 실행하고 있습니다. 그 이유는 Cloud Dataflow가 [Apache Beam](https://github.com/apache/beam)의 배포이기 때문입니다.

   ```shell
   python -m apache_beam.examples.wordcount --output OUTPUT_FILE
   ```

4. 이제 로컬 클라우드 환경에 있는 파일 목록에서 `OUTPUT_FILE`의 이름을 확인할 수 있습니다.

   ```shell
   ls
   ```

   ![image-20220315152637405](C:\Users\dad04\Desktop\LSH\TIL\GCP\md-images\image-20220315152637405.png)

5. `OUTPUT_FILE`의 이름을 복사하고 `cat` 명령어로 캡처합니다.

   - 결과에는 파일에 포함된 각 단어와 이들이 사용된 횟수가 표시됩니다.

   ```shell
   cat OUTPUT_FILE-00000-of-00001
   ```



## 3. 원격으로 예시 파이프라인 실행

1. 이전에 만든 버킷에 BUCKET 환경 변수를 설정합니다.

   ```shell
   BUCKET=gs://example_bucket_102_test
   ```

2. `wordcount.py` 예시를 원격으로 실행

   - 출력에 메시지가 나타날 때까지 기다립니다. (`JOB_MESSAGE_DETAILED: Workers have started successfully.`)

   ```shell
   python -m apache_beam.examples.wordcount --project $DEVSHELL_PROJECT_ID \
   --runner DataflowRunner \
   --staging_location $BUCKET/staging \
   --temp_location $BUCKET/temp \
   --output $BUCKET/results/output \
   --region us-central1
   ```



## 4. 작업 성공했는지 확인

- 탐색 메뉴 열고 서비스 목록에서 `Dataflow` 선택

- **wordcount** 작업의 **상태**가 **실행 중**으로 표시됩니다.

  