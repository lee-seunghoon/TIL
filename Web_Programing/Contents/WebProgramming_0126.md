[TOC]

# BoxOffice_Data_load



## <dailyBoxOfficeSearch_HTML>

> * 영화진흥위원회에서 영화 정보 API 가져와서 웹페이지에 표현
> * Bootstap의 example 사용



* jQuery CDN 방식 사용

  ```html
  <!doctype html>
  <html lang="en">
  <head>
      <meta charset="utf-8">
      <title>BoxOffice Search</title>
  
      <!-- jQuery CDN 방식 적용 -->
      <script
              src="https://code.jquery.com/jquery-2.2.4.min.js"
              integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44="
              crossorigin="anonymous"></script>
  ```



* Bootstrap CDN 방식 사용

  ```html
  <!-- Bootstrap도 CDN 방식으로 사용할거임! -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
  
  ```

  

* bootstrap에서 제공해준 css 파일 그대로 사용

  ```html
  	<!-- Custom styles for this template -->
      <link href="css/dashboard.css" rel="stylesheet">
  ```

  ==> 예시 웹 페이지에서 'F12 --> source --> docs/5.0 --> example/dashboard 가면 발견!



* head 부분

  ```html
  <!doctype html>
  <html lang="en">
  <head>
      <meta charset="utf-8">
      <title>BoxOffice Search</title>
  
      <!-- jQuery CDN 방식 적용 -->
      <script
              src="https://code.jquery.com/jquery-2.2.4.min.js"
              integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44="
              crossorigin="anonymous"></script>
  
  
      <!-- Bootstrap도 CDN 방식으로 사용할거임! -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
  
  
      <style>
          .bd-placeholder-img {
              font-size: 1.125rem;
              text-anchor: middle;
              -webkit-user-select: none;
              -moz-user-select: none;
              user-select: none;
          }
  
          @media (min-width: 768px) {
              .bd-placeholder-img-lg {
                  font-size: 3.5rem;
              }
          }
      </style>
  
  
      <!-- Custom styles for this template -->
      <link href="css/dashboard.css" rel="stylesheet">
  
    	<!-- 내가 쓸 javascript 파일 -->  
      <script src="js/dailyBoxOfficeSearch.js"></script>
  
  </head>
  ```



* body 부분

  ```html
  <body>
  
  <header class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
      <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3" href="#">BoxOffice</a>
      <button class="navbar-toggler position-absolute d-md-none collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
      </button>
      <input class="form-control form-control-dark w-100" type="text"
             placeholder="날짜를 입력해주세요 (ex.20210101)" aria-label="Search"
             id="userInputData">
      <ul class="navbar-nav px-3">
          <li class="nav-item text-nowrap">
              <a class="nav-link" href="#"     
                 onclick="my_func()">검색</a>
          </li>
      </ul>
  </header>
  
  <div class="container-fluid">
      <div class="row">
          <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
              <div class="position-sticky pt-3">
                  <ul class="nav flex-column">
                      <li class="nav-item">
                          <a class="nav-link active" aria-current="page" href="#">
                              <span data-feather="home"></span>
                              순위조회
                          </a>
                      </li>
                  </ul>
              </div>
          </nav>
  
          <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
              <br><br>
              <!-- <예시>
              <a href="http://www.naver.com">네이버 이동</a> -->
              <!--  a element는 hyperlink를 만들어주는 element
                  href 속성 다음에 있는 url로 get방식으로 request 보낸다.-->
              <h2>일일 BoxOffice 검색 순위</h2>
              <div class="table-responsive">
                  <table class="table table-striped table-sm">
                      <thead>
                      <tr>
                          <th>순위</th>
                          <th>영화제목</th>
                          <th>누적관객수</th>
                          <th>누적매출액</th>
                          <th>개봉일</th>
                      </tr>
                      </thead>
                      <tbody id="my_tbody">
                      <tr>
                          <td>1,001</td>
                          <td>Lorem</td>
                          <td>ipsum</td>
                          <td>dolor</td>
                          <td>sit</td>
                      </tr>
                      </tbody>
                  </table>
              </div>
          </main>
      </div>
  </div>
  
  
  </body>
  </html>
  ```

  

## <dailyBoxOfficeSearch_Javascript>

> * 사용자가 입력한 날짜를 이용해서 해당 날짜에 대한 boxOffice 순위 가져오기
>* boxOffice data 가지고 있는 서버쪽에 request 해서 웹 프로그램 호출 ==> 화면 출력

```javascript
function my_func(){

	let user_date = $('#userInputData').val()
    let user_key = 'd666cbf6f3b1ff4e48517a6d1b7f3166'
    let open_api = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
}
```



* location.href 의 문제점

  ```javascript
  let user_date = $('#userInputData').val()
  let user_key = 'd666cbf6f3b1ff4e48517a6d1b7f3166'
  let open_api = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
  
  // 기존 사용 방식대로 아래처럼 불러 올 수도 있다.
  let my_url = open_api + '?key=' + user_key + '&targetDt=' + user_date
  
  // but!! page 불러올 때, 새로운 화면으로 전환...
  
  location.href = my_url
  // ==> 이렇게 하면 화면 refresh가 일어나서 원하는 작업을 할 수 없다.
  ```



### <AJAX 방식>

> * 위와 같은 문제를 해결하기 위해 JavaScript가 가지고 있는 특별한 통신방식 사용!
> * 순수 JavaScript 코드 구현을 AJAX 사용하는 것은 너무 어렵고 힘듦
> * jQuery 이용 예정
> * jQuery로 AJAX 이용할 때 javascript의 객체인 '{key : value}' 이용



> * url == 내가 호출할 서버쪽 프로그램 입력
> * type == 호출을 어떤 방식으로 할거냐? (get or post)
> * dataType == 결과 data가 어떤 형태로 오느냐 (csv, xml, json ??)
> * data == 서버에 넘겨줘야 할 data
>   - 넘겨줄 데이터가 2개여서 value 쪽에 또다시 javascript 객체 부여

```javascript
$.ajax({url : open_api,
        type : 'GET',
        dataType : 'json',
        data : {
            key : user_key,
            targetDt : user_date
        },
        success : function(result) {
            // ==> 서버로부터 결과 json을 받아왔어요.
            // ==> 함수의 인자로 json 결과가 대입된다.
            // ==> json은 단순 문자열이라서 사용하기 쉽지 않다.
            // ==> 그래서 json을 javascript 객체로 변환 가능하다. 
				   //(형식이 동일하기 때문에!)
            // ==> 감사하게 jQuery가 자동으로 받아온 json을 
            	 //javascript 객체로 변환시켜 return 해준다.
        },
    	error : function () {
            alert('뭔가 이상해요!')
        }
    })
        
```



### <API 불러온 Data 웹 적용>

```javascript
function my_func(){

	let user_date = $('#userInputData').val()
    let user_key = 'd666cbf6f3b1ff4e48517a6d1b7f3166'
    let open_api = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
}

	$.ajax({
        url : open_api,
        type : 'GET',
        dataType : 'json',
        data : {
            key : user_key,
            targetDt : user_date
        },
        success : function(result) {
            
            $('#my_tbody').empty()           
            // ==> 기존 목록 지우기 위해 tbody tag 후손 모두 삭제
            
            let movie_list = result['boxOfficeResult']['dailyBoxOfficeList']
            for(let i=0; i<movie_list.length; i++) {
                let m_name = movie_list[i].movieNm
                let m_rank = movie_list[i].rank
                let m_sales = movie_list[i].salesAcc
                let m_openDt = movie_list[i].openDt
                let m_audi = movie_list[i].audiAcc

                // tr tag로 element 생성
                let tr = $('<tr></tr>')
                
                // 각 내용을 포함한 td tag element 생성
                let rank_td = $('<td></td>').text(m_rank)
                let title_td = $('<td></td>').text(m_name)
                let audi_td = $('<td></td>').text(m_audi)
                let sales_td = $('<td></td>').text(m_sales)
				let open_td = $('<td></td>').text(m_openDt)

                // 'tr' element에 자식으로 각 'td' element 추가
                tr.append(rank_td)
                tr.append(title_td)
                tr.append(audi_td)
                tr.append(sales_td)
                tr.append(open_td)
               
				// 위에서 다 만든 'tr' element를 'tbody' element 안에 자식으로 추가
                $('#my_tbody').append(tr)
            }
        },
        error : function () {
            alert('뭔가 이상해요!')
        }
    })

}
```



### <삭제 버튼 만들고 적용>

```javascript
$.ajax({
        url : open_api,
        type : 'GET',
        dataType : 'json',
        data : {
            key : user_key,
            targetDt : user_date
        },
        success : function(result) {
            $('#my_tbody').empty()
            
            let movie_list = result['boxOfficeResult']['dailyBoxOfficeList']
            for(let i=0; i<movie_list.length; i++) {
                let m_name = movie_list[i].movieNm
                let m_rank = movie_list[i].rank
                let m_sales = movie_list[i].salesAcc                
                let m_audi = movie_list[i].audiAcc
                
                // 개봉일 제거
                // let m_openDt = movie_list[i].openDt

                let tr = $('<tr></tr>')
                let rank_td = $('<td></td>').text(m_rank)
                let title_td = $('<td></td>').text(m_name)
                let audi_td = $('<td></td>').text(m_audi)
                let sales_td = $('<td></td>').text(m_sales)

                // 삭제 버튼 만들고 추가하고, 이벤트 발생까지지
                let delete_td = $('<td></td>')
                let delete_button = $('<input />').attr('type','button')
                .attr('value','삭제')
                
                // 이벤트 발생 부여 ==> .on('실행 event', function(){})
                delete_button.on('click',function(){
                    // ==> 지금 이 버튼의 element를 기준으로
                    // ==> 부모, 부모 element로 올라가서 싹지우기
                    // ==> td ==> tr ==> remove
                    $(this).parent().parent().remove()
                })
                
                // delete_td 에 delete_button element 자식으로 추가
                delete_td.append(delete_button)

              
                // 'tr' element에 자식으로 각 element 추가
                tr.append(rank_td)
                tr.append(title_td)
                tr.append(audi_td)
                tr.append(sales_td)
             
                $('#my_tbody').append(tr)
            }
        },
        error : function () {
            alert('뭔가 이상해요!')
        }
    })

}
```



### <Kakao REST_API AJAX 방식으로 불러오기>

```javascript
function my_search() {
    let keyword = '영화 포스터 건축학개론'
    let kakao_url = "https://dapi.kakao.com/v2/search/image"
    
    // AJAX 방식 활용
    $.ajax({
        url : kakao_url,
        type : 'GET',
        dataType : 'json',
        data : {
            query : keyword,
            size : 10
        },
        
        // kakao API 불러올 때 차이점 이런게 힘듦 ㅜㅜ
        // headers를 내가 어떻게 알지?        
        headers : {
            Authorization : 'KakaoAK 7a3ed81af7c2aa2be7912bbb20b5f70b'
        },
        
        success : function(result) {
            alert('성공적으로 호출!')
            let img_url = result['documents'][1]['thumbnail_url'];
            let image = $('<img />').attr('src', img_url);
            $('#myDiv').append(image);

        },
        error : function () {
            alert('뭔가 이상해요')
        }

    })
}
```

* 위 js와 연동되는 html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script
            src="https://code.jquery.com/jquery-2.2.4.min.js"
            integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44="
            crossorigin="anonymous"></script>
    <script src="js/kakao_api_search.js"></script>
</head>
<body>
    <div id="myDiv"></div>
    <input type="button" value="검색엔진"
           onclick="my_search()">
</body>
</html>
```



### <BoxOffice 영화순위 표에 영화 포스터 불러오기>

* 해당 html

```html

<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>BoxOffice Search</title>

    <!-- jQuery CDN 방식 적용 -->
    <script
            src="https://code.jquery.com/jquery-2.2.4.min.js"
            integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44="
            crossorigin="anonymous"></script>


    <!-- Bootstrap도 CDN 방식으로 사용할거임! -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>


    <style>
        .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }
    </style>


    <!-- Custom styles for this template -->
    <link href="css/dashboard.css" rel="stylesheet">

    <script src="js/dailyBoxOfficeSearch.js"></script>

</head>
<body>

<header class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
    <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3" href="#">BoxOffice</a>
    <button class="navbar-toggler position-absolute d-md-none collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <input class="form-control form-control-dark w-100" type="text"
           placeholder="날짜를 입력해주세요 (ex.20210101)" aria-label="Search"
           id="userInputData">
    <ul class="navbar-nav px-3">
        <li class="nav-item text-nowrap">
            <a class="nav-link" href="#"

               onclick="my_func()">검색</a>
        </li>
    </ul>
</header>

<div class="container-fluid">
    <div class="row">
        <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
            <div class="position-sticky pt-3">
                <ul class="nav flex-column">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">
                            <span data-feather="home"></span>
                            순위조회
                        </a>
                    </li>
                </ul>
            </div>
        </nav>

        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
            <br><br>            
            <h2>일일 BoxOffice 검색 순위</h2>
            <div class="table-responsive">
                <table class="table table-striped table-sm">
                    <thead>
                    <tr>
                        <th>순위</th>
                        <th>영화제목</th>
                        <th>포스터</th>
                        <th>누적매출액</th>
                        <th>포스터보기</th>
                    </tr>
                    </thead>
                    <tbody id="my_tbody">
                    <tr>
                        <td>1</td>
                        <td>건축학개론</td>
                        <td></td>
                        <td>99999999</td>
                        <td><input type="button" value="보기"></td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </main>
    </div>
</div>


</body>
</html>

```



* 해당 JavaScript (jQuery)

```javascript
function my_func(){
    

    let user_date = $('#userInputData').val()
    let user_key = 'd666cbf6f3b1ff4e48517a6d1b7f3166'
    let open_api = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
    
    $.ajax({
        url : open_api,
        type : 'GET',
        dataType : 'json',
        data : {
            key : user_key,
            targetDt : user_date
        },
        success : function(result) {
            $('#my_tbody').empty()
            
            let movie_list = result['boxOfficeResult']['dailyBoxOfficeList']
            for(let i=0; i<movie_list.length; i++) {
                let m_name = movie_list[i].movieNm
                let m_rank = movie_list[i].rank
                let m_sales = movie_list[i].salesAcc
                

                let tr = $('<tr></tr>')
                let rank_td = $('<td></td>').text(m_rank)
                let title_td = $('<td></td>').text(m_name)
                let img_td = $('<td></td>')
                let sales_td = $('<td></td>').text(m_sales)

             
                // 포스터 보기 버튼
                let poster_td = $('<td></td>')
                let poster_button = $('<input />').attr('type','button')
                    .attr('value','보기')
                
                // ==> poster button을 클릭하면 발생할 event 설정
                poster_button.on('click',function(){
                    let keyword = '영화 포스터' + m_name;
                    let kakao_url = "https://dapi.kakao.com/v2/search/image"

                    $.ajax({
                        url : kakao_url,
                        type : 'GET',
                        dataType : 'json',
                        data : {
                            query : keyword,
                            size : 10
                        },
                        headers : {
                            Authorization : 'KakaoAK 7a3ed81af7c2aa2be7912bbb20b5f70b'
                        },
                        success : function(result) {
                            let img_url = result['documents'][2]['thumbnail_url'];                            
                            let image = $('<img />').attr('src', img_url);
                            img_td.append(image);

                        },
                        error : function () {
                            alert('뭔가 이상해요')
                        }

                    })

                })
                poster_td.append(poster_button)
              
                // 'tr' element에 자식으로 각 element 추가
                tr.append(rank_td)
                tr.append(title_td)
                tr.append(img_td)
                tr.append(sales_td)
                tr.append(poster_td)
                
                $('#my_tbody').append(tr)
            }
        },
        error : function () {
            alert('뭔가 이상해요!')
        }
    })

}
```



---



## <jQuery 추가 기능>



* html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script
            src="https://code.jquery.com/jquery-2.2.4.min.js"
            integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44="
            crossorigin="anonymous"></script>
    <script src="js/jQuery_sample04.js"></script>
    <style>
        /* class가 myStyle인 모든 element에 적용 */
        .myStyle {
            background-color: yellow;
            color: red;
        }
    </style>
</head>
<body>
    <!--  jQuery Event 처리  -->
    <!--  가장 쉬운 이벤트 처리방법은 html이 가지고 있는 이벤트 관련 속성을 이용!  -->
        
    <!-- 'event' : 'onmouseover' == mouse 커서가 위에 올라와 있는 상태 -->
    <!-- 'event' : 'onmouseleave' == mouse 커서가 떠난, 벗어난 상태 -->
    <h1 onmouseover="set_style()"
        onmouseleave="release_style()">여기는 H1 영역입니다.</h1>

    <h2>소리없는 아우성!</h2>
    <input type="button" value="클릭"
           onclick="add_event()">

    <!--  똑같은 tag명인데, 각 element마다 클릭(이벤트) 시행하고 싶을 때   -->
    <h3>사용자 이름 : 아이유</h3>
    <h3>사용자 이름 : 김연아</h3>
</body>
</html>
```



* 위 html 연동 javascript

```javascript

function set_style() {
    // ==> 속성으로 class 추가
    $('h1').addClass('myStyle')
}

function release_style() {
    // ==> 속성 class를 삭제
    $('h1').removeClass('myStyle')
}

function add_event() {
    // h2을 찾아서 이벤트 처리할 수 있는 능력을 부여해주는 함수!!
    // 이벤트발생 함수 ==> .on('어떤이벤트?', '저 이벤트 시행됐을 때, 어떤 기능 수행?')
    // function( 앞에 시행한 이벤트 객체가 전달된다. )
    $('h2').on('click', function(event){
        alert('h2가 클릭되었어요.')
    })
}
```



### <주의해야 할 이벤트 부여 기능>

> * 일반적으로 javascript jQuery는 html의 body부분이 호출되기 전에 먼저 읽어진다.
>   (head 부분에 있잖여~)
> * 그러므로 특정 tag를 selector로 찾는 jQuery 입력하면 못 찾는다 (함수가 아니라)
> * 그래서! .on(ready) 를 부여해줘서 이벤트 가능하게 만들어준다.

```javascript
// ==> 'document' : 전체 문서 창을 의미
// ==> 'ready'로 인해 준비상태를 만들어줘서 event 실행시 적용 가능

$(document).on('ready', function(){
    $('h3').on('click', function(event){
        //alert('클릭되었어요')
        // 이벤트가 발생했을 때 어떤 element에서 event가 발생했는지 판단 파악 필요!
        
        // 'this'는 현재 이벤트가 발생한 element를 지칭함!
        alert($(this).text())
    })
})
```

​	