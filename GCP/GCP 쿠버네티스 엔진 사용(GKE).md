# GCP 쿠버네티스 사용

- GKE를 활용하여 컨테이너 생성 및 어플리케이션 배포 실습
- GKE : Google 인프라를 사용하여 컨테이너식 애플리케이션을 배포, 관리 및 확장 가능한 관리형 환경 제공



## 쿠버네티스 기능

- 컨테이너 클러스터와 상호작용 할 수 있는 매커니즘 제공
- 자동 관리
- 애플리케이션 컨테이너의 모니터링 및 활성 여부 조사
- 자동 확장
- 순차적 업데이트



## GKE 클러스터 장점

- `Compute Engine` 인스턴스를 위한 부하 분산
- 노드 풀로 클러스터 안에 `하위 노드 집합을 지정`하여 유연성 강화
- 클러스터에서 노드 인스턴스 개수 `자동 확장`
- 클러스터에서 노드 소프트웨어 `자동 업그레이드`
- `노드 자동 복구`로 노드 상태 및 가용성을 유지 관리 용이
- Cloud Monitoring을 통해 로깅 및 모니터링으로 클러스터 현황에 대한 `가시성` 확보



## Work1 기본 컴퓨팅 영역 설정

- 컴퓨팅 영역(Computing Zone)이란 리전 내에 대략적으로 클러스터와 리소스가 존재하는 `위치`
  ex) `us-central1-a`는 `us-central1` 이란 리전에 속한 영역이다.

- 컴퓨팅 영역의 기본값을 `us-central1-a`로 설정하려면 Cloud shell에서 다음 명령어 수행
  <입력>

  ```shell
  gcloud config set compute/zone us-central1-a
  ```

  <출력>

  ```shell
  # 정상 출력
  Update property [컴퓨팅/영역]
  Updated property [compute/zone].
  ```



## Work2. GKE 클러스터 만들기

- `클러스터` : 1개 이상의 클러스터 마스터 머신과 노드라는 다수의 작업자 머신으로 구성

- `노드` : 클러스터를 구성하기 위해 필요한 쿠버네티스 프로세스 실행하는 `Compute Engine VM 인스턴스`

- 클러스터를 생성하기 위해 다음 명령어 실행. 단, `[CLUSTER-NAME]`은 선택한 클러스터 이름(예:`my-cluster`)으로 바꾼다

  ```shell
  gcloud container clusters create [CLUSTER-NAME]
  ```

  ※ 표시되는 경고는 모두 무시해도 괜찮다. 클러스터 생성이 완료되는 데 몇 분이 걸릴 수 있다.

  ```shell
  # 정상 출력
  NAME: my-cluster
  LOCATION: us-central1-a
  MASTER_VERSION: 1.21.6-gke.1500
  MASTER_IP: 130.211.220.245
  MACHINE_TYPE: e2-medium
  NODE_VERSION: 1.21.6-gke.1500
  NUM_NODES: 3
  STATUS: RUNNING
  ```

  

## Work3. 클러스터의 사용자 인증 정보 얻기

- 클러스터와 상호작용하기 위해서는 `사용자 인증 정보` 필요

- 클러스터 인증을 위해 다음 명령어 실행(`[CLUSTER-NAME]`은 사용할 클러스터 이름으로 변동)

  ```shell
  gcloud container cluster get-credentials [CLUSTER-NAME]
  ```

  ```shell
  # 정상 출력
  Fetching cluster endpoint and auth data.
  kubeconfig entry generated for my-cluster.
  ```

  

## Work4. 클러스터에 애플리케이션 배포

- 클러스터에 `컨테이너식 애플리케이션 배포`

- GKE는 `Kubernetes 객체`를 사용하여 클러스트의 리소스를 만들고 관리한다.
- 웹 서버와 같은 `스테이트리스 애플리케이션`을 배포할 때는 k8s에서 `배포 객체` 사용
- `서비스 객체`는 인터넷에서 애플리케이션에 액세스하기 위한 규치과 부하 분산 방식을 정의한다.



1. `hello-app`이라는 컨테이너 이미지에서 **새 배포** `hello-server`를 생성하기 위해 다음 명령어 수행

   ```shell
   kubectl create deployment hello-server --image=gcr.io/google-samples/hello-app:1.0
   ```

   ```shell
   # 정상출력
   deployment.apps/hello-server created
   ```

   - 위 명령어를 통해 배포 객체 생성
   - `--image` : 배포할 컨테이너 이미지 지정 (위 입력한 이미지는 Container Registry 버킷에서 가져온 예시 이미지)
   - `gcr.io/google-samples/hello-app:1.0` : 가져올 특정 이미지 버전을 의미, 버전 지정하지 않을 경우 최신 버전 사용

   

2. 애플리케이션을 외부 트래픽에 노출할 수 있는 쿠버네티스 리소스인 `Kubernetes Service` 생성

   ```shell
   kubectl expose deployment hello-server --type=LoadBalancer --port 8080
   ```

   - `--port` : 컨테이너가 노출될 포트 지정
   - `type=LoadBalancer` : 컨테이너의 Compute Engine 부하 분산기 생성

   ```shell
   # 정상출력
   service/hello-server exposed
   ```



3. `hello-server` **서비스를 검사**하려면 아래 명령어 실행

   ```shell
   kubectl get service
   ```

   ```shell
   # 정상출력
   NAME           TYPE           CLUSTER-IP      EXTERNAL-IP    PORT(S)          AGE
   hello-server   LoadBalancer   10.104.15.121   35.224.232.2   8080:32046/TCP   64s
   kubernetes     ClusterIP      10.104.0.1      <none>         443/TCP          8m54s
   ```

   ※ `EXTERNAL-IP` 열이 대기중 상태라면 위 명령어 다시 실행



4. 웹브라우저에서 애플리케이션 보려면 다음 주소 입력 ( `[EXTERNAL-IP]`는 `hello-server`의 IP로 변경)
   ```shell
   http://[EXTERNAL-IP]:8080
   ```

   정상출력 화면

   ![image-20220302113630611](C:\Users\dad04\Desktop\LSH\TIL\GCP\md-images\image-20220302113630611.png)



5. **클러스터 삭제**

   ```shell
   gcloud container cluster delete [CLUSTER-NAME]
   ```

   - 메시지가 표시되면 Y를 입력하여 확인

   ```shell
   # 정상 출력
   Deleting cluster my-cluster...done.     
   Deleted [https://container.googleapis.com/v1/projects/qwiklabs-gcp-01-002198814e88/zones/us-central1-a/clusters/my-cluster].
   ```