# Cloud Dataprep

- 데이터를 시각적으로 탐색하고 정리하여 분석할 수 있도록 준비하는 지능형 데이터 서비스
- 서버리스 형식으로 어떤 규모의 작업에도 사용할 수 있으며 인프라를 배포하거나 관리할 필요가 없습니다. 
- 코드 없이 클릭만으로 손쉽게 사용 가능



# 실습



## 1. 버킷 만들기

- `Cloud Storage` > `create Bucket `
- 버킷 이름 : `example_bucket_101_test` 



## 2. Cloud Dataprep 초기화

- **탐색 메뉴** > **Dataprep**을 선택합니다.
- Google Dataprep 서비스 약관에 동의하는 체크박스를 선택하고 **동의**를 클릭합니다.
- 체크박스를 선택하여 Trifacta와의 계정 정보 공유를 승인한 다음 **동의 및 계속하기**를 클릭합니다.
- **허용**을 클릭하여 Trifacta가 프로젝트 데이터에 액세스하도록 허용합니다.
- Trifacta에서 제공하는 Cloud Dataprep에 로그인할 때 사용할 GCP 사용자 이름을 클릭합니다. GCP 사용자 이름은 연결 세부정보 패널의 **사용자 이름**입니다.
- **허용**을 클릭하여 GCP 실습 계정에 대한 액세스 권한을 Cloud Dataprep에 부여합니다.
- 체크박스를 선택하고 **동의**를 클릭하여 Trifacta 서비스 약관에 동의합니다.
- '처음 설정' 화면에서 **계속**을 클릭하여 `기본 저장소 위치`를 만듭니다.



## 3. 흐름(Flow) 생성

- Cloud Dataprep은 `flow` 작업공간을 사용하여 데이터세트에 액세스하고 조작합니다.

- **Flows** 아이콘을 클릭한 다음 **Create** 버튼을 클릭한 다음 **Blank Flow**를 선택합니다.

  ![image-20220315142459693](C:\Users\dad04\Desktop\LSH\TIL\GCP\md-images\image-20220315142459693.png)

- **Untitled Flow**를 클릭한 다음 흐름의 이름을 지정하고 설명합니다.

- 이 실습에서는 [미국 연방 선거 관리 위원회 2016](https://www.fec.gov/data/browse-data/?tab=bulk-data)의 2016년 데이터를 사용하므로 **flow** 이름을 `"FEC-2016"`으로 지정하고 설명을 `"미국 연방 선거 관리 위원회 2016(United States Federal Elections Commission 2016)"`으로 지정하는 것이 좋습니다.

  ![image-20220315142614773](C:\Users\dad04\Desktop\LSH\TIL\GCP\md-images\image-20220315142614773.png)

- OK 클릭



## 4. 데이터셋 가져오기

- **Add Datasets**를 클릭한 다음 **Import Datasets** 링크를 선택합니다.

  ![image-20220315144659273](C:\Users\dad04\Desktop\LSH\TIL\GCP\md-images\image-20220315144659273.png)

- 왼쪽 메뉴 창에서 **Cloud Storage**를 선택하여 Cloud Storage에서 데이터세트를 가져온 다음 연필을 클릭하여 파일 경로를 수정합니다.

- **Choose a file or folder**(파일 또는 폴더 선택) 텍스트 상자에 `gs://spls/gsp105`를 입력한 다음 **Go**() 을 클릭합니다.

- **us-fec/**를 클릭합니다.

- `cn-2016.txt` 옆의 **+** 아이콘을 클릭하여 오른쪽 창에 표시되는 데이터세트를 만듭니다. 데이터세트의 제목을 클릭하고 이름을 "Candidate Master 2016"으로 바꿉니다.

- 같은 방식으로 `itcont-2016.txt` 데이터세트를 추가하고 이름을 "Campaign Contributions 2016"으로 바꿉니다.

- 오른쪽 창에 두 데이터세트가 나열되면 **Import & Add to Flow**(가져오기 및 흐름에 추가)를 클릭합니다.



## 5. Candidate  파일 준비

- 기본적으로 Candidate Master 2016 데이터세트가 선택됩니다. 오른쪽 창에서 **Edit Recipe**를 클릭합니다.

- 변환 페이지에서는 변환 레시피를 빌드하고 이를 샘플에 적용한 결과를 볼 수 있습니다. 표시되는 결과에 만족하면 데이터세트에서 작업을 실행합니다.

- 각 열 머리글에는 데이터 유형을 지정한 이름과 값이 있습니다. 플래그 아이콘을 클릭하면 데이터 유형이 표시됩니다.

- 플래그 옵션을 클릭하면 오른쪽에 **Details**(세부 사항) 패널이 열립니다

- Column5는 1990-2064년의 데이터를 제공합니다. 스프레드시트에서와 같이 column5를 넓히면 각 연도가 분리됩니다. 2016년을 나타내는 가장 큰 빈을 클릭하여 선택합니다. 그러면 이 값을 선택하는 단계가 만들어집니다.

- 오른쪽의 **Suggestions**(추천) 패널에 있는 **Keep rows**(행 유지) 섹션에서 **Add**(추가) 를 클릭하여 이 단계를 레시피에 추가합니다.

  ```
  Keep rows where(DATE(2016, 1, 1) <= column5) && (column5 < DATE(2018, 1, 1))
  ```

- Column6(State)을 마우스로 가리킨 다음 헤더에서 일치하지 않는 부분(빨간색)을 클릭하여 일치하지 않는 행을 선택합니다

- 불일치를 수정하려면 제안 패널 맨위에서 **X** 를 클릭하여 변환을 취소 한 다음에는 Column6에서 플래그 아이콘을 클릭하고 "String"열로 변경하십시오.

- 대선 후보자를 필터링합니다. 이는 column7에 값 'P'가 있는 레코드입니다. column7의 히스토그램에서 두 개의 빈을 가리키면 'H'와 'P' 값을 갖는 빈을 알 수 있습니다. 'P' 빈을 클릭합니다.

  ```
  where column7 == 'P'
  ```

  

- 오른쪽 제안 패널에서 **Add**(추가) 를 클릭하여 레시피에 대한 단계를 승인하십시오.



## Contribution 파일 join

- 조인 페이지에서 두 데이터세트의 공통 정보에 따라 현재 데이터세트를 다른 데이터세트나 레시피에 추가할 수 있습니다.

- Contributions 파일을 Candidates 파일에 조인하기 전에 Contributions 파일을 정리해야 합니다.

- 그리드 뷰 페이지 상단에서 **FEC-2016**(데이터세트 선택기)을 클릭합니다.

- 회색으로 표시된 **Campaign Contributions**를 클릭하여 선택합니다.

- 오른쪽 창에서 **Add** > **Recipe** 를 클릭한 다음 **Edit Recipe**(레시피 수정) 을 클릭합니다.

- 페이지 오른쪽 상단의 **recipe**(레시피) 아이콘을 클릭한 다음 **New step 추가**를 클릭합니다.

- 데이터세트에서 불필요한 구분 기호를 제거합니다.

- 검색창에 다음과 같은 Wrangle 언어 명령어를 삽입합니다.

  ```wrangle
  replacepatterns col: * with: ''on: `{start}}"|"{end}`
  global:true
  ```

- 변환 빌더가 Wrangle 명령어를 파싱하여 찾기 및 바꾸기 변환 필드를 채웁니다.

  ![image-20220315150326311](C:\Users\dad04\Desktop\LSH\TIL\GCP\md-images\image-20220315150326311.png)

- **Add**(추가) 를 클릭하여 해당 변환을 레시피에 추가합니다.

- 레시피에 또 다른 New step 를 추가한 다음 **New step**(새 단계)를 클릭하고 검색창에 'Join'을 입력합니다.

- 조인 페이지를 열려면 **Join datasets(데이터세트 조인하기)**를 클릭합니다.

- "Candidate Master 2016"를 클릭하여 Campaign Contributions 2016-2에 조인한 다음 오른쪽 하단에 있는 **Accept**(수락)을 클릭합니다

- 조인 키 섹션에 마우스를 올려 놓고 연필(수정 아이콘)을 클릭합니다.

  ![image-20220315150527949](C:\Users\dad04\Desktop\LSH\TIL\GCP\md-images\image-20220315150527949.png)

- Dataprep은 공통 키를 유추하는데 다양한 공통 값을 조인 키로 추천합니다.

- 키 추가 패널의 추천 조인 키 섹션에서 **'column2 = column11'**을 클릭합니다.

- **Save and Continue**(저장 후 계속) 을 클릭합니다.

- **Next**(다음) 을 클릭하고 '열' 레이블의 왼쪽에 있는 체크박스를 선택하여 두 데이터세트의 모든 열을 조인된 데이터세트에 추가합니다.

- **Review**(검토) 를 클릭 한 다음 **Add to Recipe**(레시피에 추가) 를 클릭하여 격자보기로 돌아갑니다.



## 데이터 요약

> - 열 16에 입력된 선거 자금 데이터의 총계, 평균, 항목 수를 계산하고 열 2, 24, 8의 ID, 이름, 소속 정당 데이터로 후보자를 그룹화해서 요약을 생성합니다.



1. **New step**(새 단계)를 클릭하고 **Transformation**(변환) 검색창에 다음 수식을 입력하여 집계된 데이터를 미리봅니다.

   ```
   pivot
   value:sum(column16), average(column16), countif(column16 > 0) group: column2, column24, column8
   ```

   - 조인되어 집계된 데이터의 초기 샘플이 표시됩니다. 이 샘플은 미국의 주요 대선 후보자들에 대한 요약표와 2016년 선거 자금 통계를 나타냅니다.

2. **Add**(추가) 를 클릭하여 미국의 주요 대선 후보자들에 대한 요약표와 2016년 선거 자금 통계를 확인할 수 있습니다.



## 열 이름 변경

- 열 이름을 변경하면 데이터를 더욱 쉽게 해석할 수 있습니다. **New step**(새 단계)를 클릭하여 이름 바꾸기 및 라운딩 단계를 레시피에 개별적으로 추가한 후 다음을 입력합니다.

  ```
  rename type: manual mapping: [column24,'Candidate_Name'], [column2,'Candidate_ID'],[column8,'Party_Affiliation'], [sum_column16,'Total_Contribution_Sum'], [average_column16,'Average_Contribution_Sum'], [countif,'Number_of_Contributions']
  ```

- 그런 다음 **Add**(추가)를 클릭합니다.

  선거 자금 평균값을 라운딩하는 마지막 **New step**(새 단계)를 추가합니다.

  ```
  set col: Average_contribution_Sum value:
  round(Average_Contribution_Sum)
  ```

- 그런 다음 **Add**(추가)를 클릭합니다.

  다음과 같은 결과가 나타납니다.