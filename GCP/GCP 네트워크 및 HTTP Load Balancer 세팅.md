# GCP 부하 분산기

> - 네트워크 부하 분산기와 HTTP 부하 분산기의 차이점
> - Compute Engine VM(가상 머신)에서 실행되는 애플리케이션용으로 이들 부하 분산기를 설정하는 방법
> - 네트워크 부하 분산기
> - HTTP(S) 부하 분산기



## 실습 내용

> - 네트워크 부하 분산기 설정
>
> - HTTP 부하 분산기 설정
>
> - 네트워크 부하 분산기 vs HTTP 부하 분산기 차이점





## Work1. 모든 리소스에 대한 기본 리전 및 영역 설정

1. Cloud Shell에서 기본 영역 설정
   
    ```shell
    gcloud config set compute/zone us-central1-a
    
    ```
    
2. 기본 리전을 설정
   
    ```shell
    gcloud config set compute/region us-central1
    
    ```
    





## Work2. 다중 웹 서버 인스턴스 만들기

> - 부하 분산 시나리오
> - Compute Engine VM 인스턴스 3개 생성
> - 인스턴스에 Apache 설치
> - HTTP 트래픽이 인스턴스에 도달할 수 있도록 방화벽 규칙 추가



### step1

> - 기본 영역에 새 가상 머신 3개 만들고 모두 같은 태그 지정
> - 해당 영역은 us-central1-a로 설정
> - 태그 필드를 설정하면 방화벽 규칙을 사용할 때처럼 이러한 인스턴스를 한 번에 참조할 수 있다.
> - 아래 명령어는 각 인스턴스에 Apache를 설치하고 고유한 홈페이지를 제공한다.

```shell
gcloud compute instances create www1 \\
	--image-family debian-9 \\
	--image-project debian-cloud \\
	--zone us-central1-a \\
	--tags network-lb-tag \\
	--metadata startup-script="#! /bin/bash
	  sudo apt-get update
	  sudo apt-get install apache2 -y
	  sudo service apache2 restart
	  echo '<!doctype html><html><body><h1>www1</h1></body></html>' | tee /var/www/html/index.html"

```

```shell
gcloud compute instances create www2 \\
	--image-family debian-9 \\
	--image-project debian-cloud \\
	--zone us-central1-a \\
	--tags network-lb-tag \\
	--metadata startup-script="#! /bin/bash
	  sudo apt-get update
	  sudo apt-get install apache2 -y
	  sudo service apache2 restart
	  echo '<!doctype html><html><body><h1>www2</h1></body></html>' | tee /var/www/html/index.html"

```

```shell
gcloud compute instances create www3 \\
	--image-family debian-9 \\
	--image-project debian-cloud \\
	--zone us-central1-a \\
	--tags network-lb-tag \\
	--metadata startup-script="#! /bin/bash
	  sudo apt-get update
	  sudo apt-get install apache2 -y
	  sudo service apache2 restart
	  echo '<!doctype html><html><body><h1>www3</h1></body></html>' | tee /var/www/html/index.html"

```



### step2

> - VM 인스턴스에 외부 트래픽 허용하는 방화벽 규칙 생성
>
> - 이후 인스턴스의 외부 IP 주소를 가져와 주소가 정상적으로 작동되는지 확인 필요

```shell
gcloud compute firewall-rules create www-firewall-network-lb \\
	--target-tags network-lb-tag --allow tcp:80
```



### step3

> - 아래 명령어를 통해 인스턴스를 나열하고
> - EXTERNAL_IP 열에 인스턴스의 IP 주소 표시 확인

```shell
gcloud compute instances list
```



### step4

> - curl을 사용하여 각 인스턴스가 실행 중인지 확인
> - 아래 명령어에서 `[IP_ADDRESS]`를 각 VM의 IP주소로 바꾼다.

```shell
curl http://[IP_ADDRESS]
```





## Work3. 부하 분산 서비스 구성

> - 부하 분산 서비스를 구성하면 가상 머신 인스턴스는 사용자가 구성한 고정 외부 IP주소로 전송되는 패킷을 수신한다.
>
> - Compute Engine 이미지로 만든 인스턴스틑 이 IP 주소를 처리하도록 자동으로 구성된다.



### step1

> - 부하 분산기의 고정 외부 IP 주소 생성

```shell
gcloud compute addresses create network-lb-ip-1 \
	--region us-central1
```



### step2

> 기존 HTTP 상태 확인 리소스 추가
> 

```shell
gcloud compute http-health-checks create basic-check
```



### step3

> - 인스턴스와 동일한 리전에 대상 풀을 추가한다.
> - 아래 명령어는 대상 풀을 만든 다음에 상태 확인을 사용한다.
> - 서비스가 작동하려면 상태 확인이 필요하다

```
gcloud compute target-pools create www-pool \
	--region us-central1 --http-health-check basic-check
```



### step4

> - 풀에 인스턴스를 추가한다

```shell
gcloud compute target-pools add-instances www-pool \
	--instances www1, www2, www3

```



### step5

> - 전달 규칙 추가

```shell
gcloud compute forwarding-rules create www-rule \
	--resgion us-central1 \
	--ports 80 \
	--address network-lb-ip-1 \
	--target-pool www-pool
```





## Work4. 인스턴스로 트래픽 전송

> - 전달 규칙에 트래픽을 보내고 트래픽이 여러 인스턴스에 분산되는 것을 확인
> - 부하 분산기에서 사용하는 www-rule 전달 규칙의 외부 IP 주소를 보려면 다음 명령어를 입력

```shell
gcloud compute forwarding-rules describe www-rule --region us-central1
```

> - curl 명령어를 사용하여 외부 IP 주소에 액세스(※ 아래 [IP_ADDRESS]▶ 이전 명령어에서 사용한 외부 IP 주소로 변경)

```shell
while true; do curl -m1 IP_ADDRESS; done
```

> - curl 명령어가 실행되면 인스턴스 세 개에서 무작위로 응답한다.
> - 처음에 응답이 성공하지 못하면 구성이 완전히 로드되어 인스턴스가 정상으로 표시될 때까지 30초 정도 기다린 후 다시 시도
> - Ctrl+C를 눌러 명령어 실행 중지



## Work5. HTTP 부하 분산기 생성

- `HTTP(S) 부하 분산`은 GFE(Google 프런트엔드)에서 구현
- GFE는 Google의 `전역 네트워크 및 제어 영역`을 사용하여 전역으로 분산되고 함께 운영됩니다. 
- URL이 각기 적절한 인스턴스 집합으로 라우팅되도록 `URL 규칙`을 구성할 수 있습니다. 
- 요청은 항상 사용자와 `가장 가까운 인스턴스 그룹`으로 라우팅됩니다(해당 그룹의 용량이 충분하며 요청에 적합한 그룹인 경우). 
- 가장 가까운 그룹에 용량이 충분하지 않으면 용량이 *있는* 가장 가까운 그룹으로 요청이 전송됩니다.
- Compute Engine `백엔드`로 부하 분산기를 설정하려면 VM이 인스턴스 그룹에 있어야 합니다. 
- 관리형 인스턴스 그룹은 외부 HTTP 부하 분산기의 백엔드 서버를 실행하는 VM을 제공합니다. 
- 이 실습에서는 백엔드 서버에 `자체 호스트 이름`을 제공합니다.



1. 부하 분산기 탬플릿 생성

   ```shell
   gcloud compute instance-templates create lb-backend-template \
      --region=us-central1 \
      --network=default \
      --subnet=default \
      --tags=allow-health-check \
      --image-family=debian-9 \
      --image-project=debian-cloud \
      --metadata=startup-script='#! /bin/bash
        apt-get update
        apt-get install apache2 -y
        a2ensite default-ssl
        a2enmod ssl
        vm_hostname="$(curl -H "Metadata-Flavor:Google" \
        http://169.254.169.254/computeMetadata/v1/instance/name)"
        echo "Page served from: $vm_hostname" | \
        tee /var/www/html/index.html
        systemctl restart apache2'
   ```



2. 관리형 인스턴스 그룹 생성(탬플릿 기반)

   ```shell
   gcloud compute instance-groups managed create lb-backend-group \
      --template=lb-backend-template --size=2 --zone=us-central1-a
   ```

   

3. `fw-allow-health-check` 방화벽 규칙 생성 

   - 이 규칙은 Google Cloud 상태 확인 시스템(`130.211.0.0/22` 및 `35.191.0.0/16`)의 트래픽을 허용하는 인그레스 규칙입니다. 
   - 이 실습에서는 `allow-health-check` 대상 태그를 사용하여 VM을 식별합니다.

   ```shell
   gcloud compute firewall-rules create fw-allow-health-check \
       --network=default \
       --action=allow \
       --direction=ingress \
       --source-ranges=130.211.0.0/22,35.191.0.0/16 \
       --target-tags=allow-health-check \
       --rules=tcp:80
   ```



4. 인스턴스가 실행 중이므로 고객이 부하 분산기에 연결하는 데 사용하는 전역 고정 외부 IP 주소를 설정

   ```shell
   gcloud compute addresses create lb-ipv4-1 \
       --ip-version=IPV4 \
       --global
   ```

   - 예약된 IPv4 주소 확인

   ```shell
   gcloud compute addresses describe lb-ipv4-1 \
       --format="get(address)" \
       --global
   ```



5.  부하 분산기용 상태 확인 생성

   ```shell
   gcloud compute health-checks create http http-basic-check \
   --port 80
   ```

   

6. 백엔드 서비스 생성

   ```shell
   gcloud compute backend-services create web-backend-service \
   --protocol=HTTP \
   --port-name=http \
   --health-checks=http-basic-check \
   --global
   ```

   

7. 백엔드 서비스에 인스턴스 그룹을 백엔드로 추가

   ```shell
   gcloud compute backend-services add-backend web-backend-service \
   --instance-group=lb-backend-group \
   --instance-group-zone=us-central1-a \
   --global
   ```



8. URL 맵을 만들어 들어오는 요청을 기본 백엔드 서비스로 라우팅

   ```shell
   gcloud compute url-maps create web-map-http \
   --default-service web-backend-service
   ```



9. 대상 HTTP 프록시를 만들어 URL 맵에 요청을 라우팅

   ```shell
   gcloud compute target-http-proxies create http-lb-proxy \
   --url-map web-map-http
   ```



10. 들어오는 요청을 프록시로 라우팅하는 전역 전달 규칙 생성

    ```shell
    gcloud compute forwarding-rules create http-content-rule \
    --address=lb-ipv4-1\
    --global \
    --target-http-proxy=http-lb-proxy \
    --ports=80
    ```

    