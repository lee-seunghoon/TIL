[TOC]



---

## <용어 이해>

### library 

: 특정 기능을 수행하는 코드 묶음 (ex. 함수, 클래스)
  전체적으로 내가 원하는 logic이나 algorithm을 제공해주진 않는다.

### Framework 

: library의 확장버전으로 생각하면 좋다. 전체적인 system 즉, logic이 만들어져 있다.
  사용하려면 이 framework 작동하는 방법을 배우고 익혀야 한다.

### platform 

: 다른 프로그램을 실행시켜줄 수 있는 환경이 되는 프로그램
  (ex. Windows10, Linux, Mac / Anaconda)



---

## <Web application 구현 방식>

### <Case 1_round trip>

> server-side web application 과 client-side web appication 종속
>
> ==> 이 방식을 `Round Trip` 방식이라고 함

1. web client가 web server에 `request`

2. (web server에서 프로그램 실행은 안되서) `WAS`에 위임 request. 

3. WAS는 가지고 있는 프로그램(==server-side web application) 실행한 후 
   DataBase에서 data 가져와서 `response` 
   ===> response할 때, 요청한 data 뿐만 아니라, "html + CSS + JavaScript" 
        즉, web  client 쪽에서 rendering 할 수 있는 `코드묶음`까지 다 보내준다.

4. web client 쪽에서 받고 `rendering` 할 때, web server쪽에서 준 data 안에 있는  
   "html + CSS + JavaScript"  활용.

* 단점 

  1) `serve-side` web application 에서 "html + CSS + JavaScript" 이거까지 다 작성해야 해

  2) `data 보낼 때마다.` client 쪽에서 rendering 할 수 있는 "html + CSS + JavaScript" 이거 다 포함해서 보내줘야 해서 `무거워`



### <Case 2_AJAX>

> server-side web application 과 client-side web appication 분리 구현
>
> ==> `AJAX` 방식 (single page application 이라고도 함.)

1. client-side web application을 response 할 수 있는 server에 `request`
2. "html + CSS + JavaScript" 실행시켜주는 프로그램 run `response`
3. data 가져올 수 있는 server에 `request`
4. web server는 `WAS`에 위임 `request`
5. WAS에서 server-side web application 실행해서 data만 `자료구조 형식(json, csv 등)`으로
   `response`
6. web server에서 그대로 web client쪽으로 `response`
7. web client 쪽에서 받은 `data(json)` 가지고 처음에 response 받았던 client-side web application 실행해서 `rendering`



---



## <Case 2 실습>

### boxoffice open api data 가져오기

* boxoffice.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    
    <!--jQuery 라이브러리를 이용하기 위해서 CDN 방식(import와 같은 것) 이용하기 -->
    <!--jQuery 사이트 => download 쪽에서 => CDN방식 => 2.x버전 minified => 복붙 -->
    <script
            src="https://code.jquery.com/jquery-2.2.4.min.js"
            integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44="
            crossorigin="anonymous"></script>
    
    <!--src에 javascript 파일을 매칭시켜주면 이제 그 안에 있는 js 코드 사용 가능-->
    <script src="js/my_script.js">
    </script>
</head>
<body>
    일일 박스오피스 순위를 알아보아요
    <br><br>
    key : <input type='text' id='userKey'>
    <br><br>
    날짜 : <input type='text' id='userDate'>
    <br><br>
    
    <!-- 버튼 박스 만들기 -->
    <input type='button' value='조회'
           onclick='hello()'>
    
</body>
</html>
```



* my_script.js

```javascript
function hello() {
    // alert() == 경고창 띄워주는 method 
    alert('버튼이 클릭되었어요')
    
    // $ ==> jQuery 사용한다는 의미
    // # ==> id 사용 한다는 selector
    // .val() ==> 값을 불러달라는 method
    
    user_key = $('#userKey').val()
    user_date = $('#userDate').val()
    
    // 영화진흥위원회에서 가져오 open api 주소
    open_api = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
    
    // 실제 호출 할 주소 
    open_url = open_api + '?key=' + user_key + '&targetDt' + user_date
    
    // 현재 페이지를 바꿔주는 명령어
    location.href = open_url
}
```



---



## <Javascript 간단 정리>

### 1. 변수 선언

```javascript
// 변수 선언은 파이썬과 거의 비슷하다.
// 변수 앞에 일반적으로 var 이라는 keyword 잡아준다.
// 최근 버전 update 후 let로 사용하라고 권장.
// ';' 세미콜론의 의미는 '여기까지 해당 statement가 종료'

let tmp1 = 'sample';	// string
let tmp2 = 10;			// number
let tmp3 = true;		// boolean type (python과 다르게 소문자!)
let tmp4 = [1,2,3,4]	// array (python의 list와 비슷하지만 array라고 표현!)

```



### 2. 변수 출력하고 싶을 때 2가지 방법

```javascript
// 1) alert() 이용하여 변수 출력 가능

alert(tmp1)
// ==> 하지만 이것은 권장하는 방법 아님, 왜냐면
// ==> blocking method라는 특성을 가져서 이 함수 작동 후 특정 클릭 안해주면 다음 코드로 안넘어감.


// 2) consol.log()
consol.log('변수의 값 : ' + tmp1)
// browser 창에서 f12 눌러 consol tap에서 변수 확인 가능
```



### 3. Javascript 객체

> python의 dict와 같은 구조
>
> data 표현 방식은 json으로 return

```javascript
let obj = { name : '홍길동',
            age : 23}

consol.log(obj.name)
// obj 객체중 name의 값을 출력
```



### 4. 함수 만들기

```javascript
funcion add(x,y) {
    return x+y
}

alert(add(10,20))
```



---



## <HTML 간단정리>

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
    <script src = 'js/jQuery_exec.js'></script>
</head>
<body>
    <!-- element : html 구성요소 ('시작tag' 부터 '끝tag' 까지) -->
    <!-- tag : <>로 구성되는 html 요소 -->
    <!-- element의 종류는 크게 2가지 있다.
         block level element : element가 한 line을 완전히 차지한다.
         inline element : element가 해당 내용만 영역을 차지한다.-->
    
    <h1>여기는 h1입니다.(headline 형태 크기와 모양)</h1>
    
    <ul>   <!-- unordered list (<ul>은 순서가 없는 list 형식) -->
           <!-- <li>는 그 list 안의 값을 보여주는 tag -->
        
        <li class="region">서울</li>  
        <!-- class 값을 줄 수 있다 -->
        
        <li id="inchon">인천</li>
        <!-- id 값을 줄 수 있다. -->
        
        <li>부산</li>
    </ul>

    <ol>  <!-- 순서가 있는 list 표현 -->
        <li>김연아</li>
        <li>홍길동</li>
        <li>아이유</li>
    </ol>

    <!-- <div>는 그 안에 있는 내용을 논리적인 영역으로 구분 / div는 block level element -->
    <div> 여기는 div 영역 </div>

    <!-- <span> 또한 div 같이 영역 잡는 tag / span영역은 inline element다! -->
    <span class="region"> 여기는 span 영역 </span>

    <!-- img tag (끝 tag가 없다./ input이랑 비슷하네)-->
    <img src = 'img/english.jpg'>
    <br><br>
    <input type = 'button' value="클릭!"
            onclick='my_func()'>

</body>
</html>
```



---



## <jQuery 정리_selector>

### <기본>

```javascript
// selector란 HTML element를 지칭하는 특수한 표기법을 의미
$('selector').method(); // ==> selector가 의미하는 element(객체 같은 놈)를 찾겠어
```



### 1) 전체 선택자 : '*'

```javascript
$('*').css('color', 'red'); 

// ==> jQuery 이용해서 body 안에 있는 모든 element를 다 찾아
// ==> .css() : 스타일을 바꾸는 jQuery 함수
```



### 2) 태그 선택자 : '태그명'

```javascript
$('span').remove() // ==> span tag명 가지고 있는 것들 다 지워버려
$('li').css('background-color', 'yellow'); // ==> li tag 배경색 다 노랑으로
```



### 3) ID 선택자 : ID 속성을 이용해서 element를 선택

```javascript
//'#'으로 ID를 찾는다.
//.text() ==> 해당 element에 있는 text를 바꾼다.

$('#inchon').text('text를 바꿨습니다.');
// ==> id 값이 'inchon'인 tag 안의 text를 바꾼다는 의미
```



### 4) class 선택자 : class 속성을 이용해서 선택

```javascript
//'.'으로 class를 찾는다.

$('.region').css('color', 'blue');
// ==> class가 'region'인 tag만 모두 글자색을 파랑으로
```



### 5) 구조 선택자 : 부모, 자식, 형제 관계를 이용해서 선택

```javascript
//$('부모tag > 자식tag') ==> 부모 tag에 속해 있는 자식 중 지정한 자식tag만 불러와

$('ol > li').css('color', 'red')
// ==> <ol> tag에 속해 있는 tag 중 <li>라는 자식 tag들 불러와서 실행
```