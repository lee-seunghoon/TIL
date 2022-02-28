# GCP 가상머신(VM) 만들기

- Cloud Shell은 다양한 개발 도구가 탑재된 가상 머신으로, 5GB의 영구적인 저장소를 제공하고 Google Cloud에서 실행된다. Cloud Shell을 통해 comand line으로 GCP 리소스에 액세스 할 수 있다.



## Work1. Cloud Shell 명령어



- 사용 중인 계정 이름 목록

```shell
gcloud auth list
```

- 예시 출력

```shell
Credentialed accounts:
- <myaccount>@<mydomain>.com (active)

Credentialed accounts:
- google1623327_student@qwiklabs.net
```



- 프로젝트 ID 목록

```shell
gcloud config list project
```

- 예시출력

```shell
[core]
project = <project_ID>

[core]
project = qwiklabs-gcp-44776a13dea667a6
```



## Work2. Cloud VM 새 인스턴스 만들기

- 아래 이미지 정보 참고 (가벼운 Default)

  ![image-20220228150651382](C:\Users\dad04\Desktop\LSH\TIL\GCP\md-images\image-20220228150651382.png)



## Work3. NGINX 웹 서버 설치

- SSH 터미널에서 root 액세스

```SSH
sudo su -
```



- `root` 사용자로 OS 설치

```SSH
apt-get update
```



- NGINX 실행 중인지 확인

```SSH
ps auwx | grep nginx
```



- NGINX 정상 설치 확인 방버

  - cloud console > VM instances 에서 인스턴스의 External IP로 접속하면 아래 이미지로 설치 성공 확인

    ![image-20220228151831706](C:\Users\dad04\Desktop\LSH\TIL\GCP\md-images\image-20220228151831706.png)



## Work4. gcloud로 새 인스턴스 만드는 방법

- Google console을 사용하는 대신 Cloud Shell에 사전 설치 돼 있는 명령줄 도구인 `gcloud`를 활용해서 새 인스턴스를 만들 수 있습니다.
- `Cloud Shell`은 Debian 기반 가상 머신으로, gcloud, git 과 같은 개발도구가 로드돼 있으며, 5GB의 영구적인 홈 디렉토리를 제공합니다.

---



- Cloud Shell에서 gcloud로 가상 머신 인스턴스 만들기

  ```shell
  gcloud compute instances create gcelab2 --machine-type n1-standard-2 --zone us-central1-f
  ```



- 모든 기본값 확인 위한 명령어

  ```shell
  gcloud compute instances create --help
  ```



- SSH를 사용하여 gcloud 통해 인스턴스 연결

  - 이럴 경우 영역을 추가 해야 하며, 옵션을 전역으로 설정한 경우에는 `--zone` 플래스를 생량해야 한다.

    ```shell
    gcloud compute ssh gcelab2 --zone us-central1-f
    ```

    

