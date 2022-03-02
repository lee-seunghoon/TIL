# GCP Cloud Shell 및 gcloud 시작하기



## 1. 환경 구성



- 기본 리전 및 영역 확인

  ```shell
  gcloud config get-value compute/zone
  gcloud config get-value compute/region
  ```

  (만약 unset으로 나오면 기본 영역이나 리전이 설정되지 않은 것)



- 프로젝트 ID 설정

  ```shell
  gcloud comute project-info describe --project <your_project_ID>
  ```

  

## 2. 환경 변수 설정

- 환경을 정의하는 환경 변수는 API 또는 실행 파일이 포함된 스크립트를 작성할 때 시간 절약에 도움을 준다.



1. project ID 설정

   (위에서 `gcloud comute project-info describe` 로 세팅한 project ID를 기입한다)

   ```shell
   export PROJECT_ID=<your_project_ID>
   ```

2. 영역을 저장할 환경 변수를 만들고 위 `gcloud comute project-info describe` 명령어의 영역에 해당하는 값으로 ZONE을 세팅한다.

   ```shell
   export ZONE=<your_zone>
   ```

3. 변수가 적절하게 설정되었는지 확인하기 위해 아래 명령어 사용

   ```shell
   echo $PROJECT_ID
   echo $ZONE
   ```

   



## 3. gcloud로 새 가상 머신 만들기

1. `ZONE`은 위 `gcloud comute project-info describe`로 세팅한 프로젝트의 영역을 입력한다.

   ```shell
   gcloud compute instances create gcelab2 --machine-type n1-standard-2 --zone $ZONE
   ```



**명령어 세부 정보**

- `gcloud comute`를 사용하여 Compute Engine 리소스 관리를 Compute Engine API보다 더 간단하게 관리할 수 있다.
- `instances create`는 새 인스턴스를 만든다.
- `gcelab2`는 VM의 이름
- `--machine-type` 플래그는 머신 유형을 `m1-standard-2`로 지정한다.
- `--zone` 플래그는 VM이 생성되는 위치를 의미한다.



## 4. gcloud 명령어 살펴보기

1. 간단한 사용 가이드라인

   ```shell
   gcloud -h
   ```

2. 자세한 도움말

   ```shell
   gcloud config --help
   ```

   ```shell
   gcloud help config
   ```

3. 구성 목록 확인

   ```shell
   gcloud config list
   ```

4. 모든 속성 및 각 설정 확인

   ```shell
   gcloud config list --all
   ```

5. 구성요소 나열

   ```shell
   gcloud components list
   ```

   

## 5. gcloud 구성요소 설치

- 자동 완성 모드로 `gcloud interactive` : 명령어 및 플래그를 자동으로 추천, 명령어 입력 시 하단에 인라인 도움말 스니펫 표시



1. 베타 구성요서 설치

   ```shell
   sudo apt-get install google-cloud-sdk
   ```

2. `gcloud interactive` 모드 사용

   ```shell
   gcloud beta interactive
   ```

3.  `your_vm`을 기존 vm으로 변동 Test

   ```shell
   gcloud compute instances describe <your_vm>
   ```

   

## 6. 홈 디렉토리 사용

- Cloud Shell 홈 디렉토리의 콘텐츠는 가상 머신을 종료했다가 다시 시작하더라도 모든 Cloud Shell 세션의 프로젝트에서 그대로 유지된다.



1. 현재 작업 디렉토리 변경

   ```shell
   cd $HOME
   ```

2. `vi` 텍스트 편집기를 사용하여, `.bashrc` 구성 파일 연다

   ```shell
   vi ./.bashrc
   ```

3. 편집기 종료하려면 **ESC** 키를 누른 다음 `:wq`를 누른다.