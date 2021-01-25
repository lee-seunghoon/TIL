[TOC]



---

## <HTML_update>

### form(사용자 입력 양식) 

> 사용자 입력 양식의 목적 : 사용자로부터 데이터 입력 받아서 서버로 전송!
>
> ==> 'form' tag를 통해 사용자 입력 장식으로 지정!
>
> ==> <form action='#' method="post">
>
> 	- action 뒤에는 data를 넣어 줄 서버쪽 프로그램명을 입력! (지금은 없어서 #)
> 	- method 뒤에는 요청방식을 입력!

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
    <script src="js/jQuery_sample01.js"></script>
</head>
<body>

    <div>
        <ul>
            <li id="apple">사과</li>
            <li id="pineapple">파인애플</li>
            <li class="mylist">참외</li>
        </ul>

        <!-- 그냥 input과 다르다! 서버와 연결하는 양식! -->
        <form action="#" method="post">
            <input type="text" id="uId" size="20">
        </form>
        
        <ol>
            <li class="mylist">고양이</li>
            <li class="mylist">호랑이</li>
            <li class="mylist">강아지</li>
        </ol>
    </div>

    <input type="button" value="click"
           onclick="my_func()">
</body>
</html>
```



### <style 지정>

* div로 지정

  > 각 div에 style이 다 적용된다.
  >
  > 하지만 style은 일반적으로 class를 활용해서 지정해준다.

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
    <script src="js/jQuery_sample02.js"></script>

    <style>
        
        div {
            width : 100px;
            height : 50px;
            background-color: yellow;
        }
    </style>
</head>
<body>
    <div>이것은 소리없는 아우성! <br><br></div>
    <div>
        <ol>
            <li>홍길동</li>
            <li>김연아</li>
        </ol>
    </div>
</body>
</html>
```



* class로 지정

  > 아래 코드에서 class를 myStyle로 가지고 있는 element에게만 적용될 것이다.

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
    <script src="js/jQuery_sample02.js"></script>

    <style>
        /*class 속성 이용해서 지정하는 것이 일반적이다.*/
        .myStyle {
            width : 300px;
            height : 100px;
            background-color: yellow;
        }
    </style>
</head>
<body>
    <div>이것은 소리없는 아우성! <br><br></div>
    <div class="myStyle">
        <ol>
            <li>홍길동</li>
            <li>김연아</li>
        </ol>
    </div>
</body>
</html>
```



### <속성을 활용해 button 활성화 막기>

> disabled 라는 속성을 활용해서 비활성화 할 수 있다.

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
    <script src="js/jQuery_sample02.js"></script>

</head>
<body>
    <!-- 속성을 이용해서 버튼 활성화 막기 -->
    <input type="button" value="클릭되나요?"
            disabled="disabled">

    <input type="button" value="클릭"
           onclick="my_func()">
    <input type="button" value="스타일제거"
            onclick="remove_func()">
</body>
</html>
```





---

## <jQery_다양한 기능>

### <.text()>

> tag 사이에 있는 글자를 가지고 오고 싶을 때

```javascript
function my_func() {
    console.log($('#apple').text()) 
    // ==> tag 사이에 있는 글자 가지고 오고 싶을 때 : .text()
    // ==> console.log : console 창에 출력
    
    $('#pineapple').text('이 글자로 대체') 
    // ==> .text() 안에 인자가 있으면 그 글자로 대체

    console.log($('ul > .mylist').text())
    // ==> ul 자식 tag 중, mylist class 찾아서 그 text 찾아옴
```



### <.val()>

> 입력박스 상자 안에 있는 값을 가져오고 싶을 때
>

```javascript
 console.log($('#uId').val())
// ==> uId 라는 id 값을 가진 element의 값을 가져온다.
// ==> 주로 text 박스의 값을 가져올 때 쓴다.
```



### <.attr()>

> 속성 값을 알아낼 때 쓴다.
>
> 해당 속성의 값 또한 바꿀 수 있다.

```javascript
console.log($('input[type=text]').attr('id'))
// ==> input tag 중 type속성을 text로 가지고 있는 element의 id 속성의 값을 알아낼 수 있다

$('input[type=text]').attr('size', 30)
// ==> input tag 중 type속성을 text로 가지고 있는 element의 size 속성의 값을 30으로 변경한다.
```



### <원하는 element indexing 하기>

```javascript
// 특정 tag의 element 중에서 첫번째 값 가져오기
console.log($('ol>li:first').text())
// ==> ol의 자녀 li 중 첫번 째 값.

// 특정 tag의 element 중에서 마지막 값 가져오기
console.log($('ol>li:last').text())

// 첫번째 값 바로 다음에 다오는 값 가져오기
console.log($('ol>li:first+li').text())

// 순번으로 콕 집어서 가져오기
 console.log($('ol > li:eq(1)').text())
```



### <동일한 element에서 각각의 값을 가져올 때>

> 형식 : .each(function(idx,item) { 값들 어떻게 출력할건지 })
>
> 각각의 값을 순번과 그 element 자체를 return해준다.
>
> idx == index / item == 하나의 tag 전체 element
>
> 즉, each는 for문처럼 각각의 값을 하나씩 가져와서 처리해준다.

```javascript
$('ol > li').each( function(idx,item) {
	console.log((idx + 1) + '번째 ' + $(item).text() + '입니다.')
})
```



### <함수의 종류_simple 설명>

* 명시적 함수

  > 함수에 이름이 있다.

* 묵시적 함수 ( == lambda 함수)

  > 묵시적 함수는 독립적으로 사용하지 못하고 변수에 담아서 사용한다.
  >
  > 즉, 함수를 하나의 값으로 인식한다 ==> 어려운 말로, 'first class'
  >
  > 그래서 이 묵시적 함수는 하나의 값으로 인식되기 때문에 다른 함수의 인자로 사용 X

```javascript
// 예시
let tmp = function() {}
```



### <css의 치명적인 담점>

```javascript
function my_func() {
    $('div').css('color','red')
    $('div').css('background-color','yellow')
    
    // .css()의 치명적인 단점! ==> 다시 rendering한다.
    // 즉, 함수 실행할 때마다, 다시 그림을 그린다.
```



### <지정한 tag에 대해 class 새로 만들어주는 함수>

> .addClass('새로 만들 class 명')

```javascript
function my_func() {
    $('div').addClass('myStyle')
}
```



### <각 tag의 속성을 지우고 싶을 때>

> .rmoveAttr('지우고 싶은 속성 명')

```javascript
function my_func() {
    $('input[disabled=disabled]').removeAttr('disabled')
}
// ==> input element 중 disabled라는 속성을 가지고 있는거 찾아서
// ==> 그중 disabled 속성만 지운다.
```



### <tag명과 class 합쳐서 지정하여 element 지우고 싶을 때>

```javascript
function my_func() {
    $('div.myStyle').remove()
}
// ==> div tag 중 'myStyle'을 class로 가지고 있는 element를 찾아서
// ==> 삭제
```



### <후손 element만 싹 삭제하고 싶을 때>

> .empty()

```javascript
function my_func() {
    $('div.myStyle').empty()
}
// ==> div 중 myStyle class 가지고 있는 맨위 element만 존재하고 그 밑 후손 element 모두 삭제한다.
```



### <class를 지우고 싶을 때>

> .removeClass('지우고 싶은 class 명')

```javascript
function remove_func() {
    $('div').removeClass('myStyle')
}
// ==> div element 찾아서 그 중 myStyle을 class로 가지고 있는 것들, class를 지워
```



### <없는 element를 새로 만들고 싶을 때>

```javascript
function my_func() {
    
	// 일반적으로 시작, 끝 tag 모두 가지고 있는 tag명
	let my_div = $('<div></div>').text('추가하고 싶은 내용')
    
    // 끝 tag가 없는 tag명
    let my_img = $('<img />').attr('src', 'img/english.jpg')
    // ==> 즉 이건, <img src='img/english.jpg'> 이런 이미지 파일 사용한다는 의미
    
    
```



---



## <jQuery 기능 중 새로운 element를 기존 element에 붙이고 싶을 때>

### 1. append()

> 무조건 자식으로 붙이고, 매 마지막 자식으로 붙인다.

```javascript
function my_func(){
    let my_li = $('<li></li>').text('아이유')
    $('ul').append(my_li)
}
// ==> ul element의 자식 element로 맨 마지막에 추가
```



### 2. prepend()

> 자식으로 붙이고, 맨 처음 자식으로 붙인다.

```javascript
function my_func(){
    let my_li_pre = $('<li></li>').text('이승훈')
    $('ul').prepend(my_li_pre)
}
```



### 3. after()

> 형제로 붙이고, 지정한 element 다음 형제 element로 추가

```javascript
function my_func(){
    let my_li_after = $('<li></li>').text('Alexa')
    $('ul>li:eq(2)').after(my_li_after)
}
```



### 4. before()

> 형제로 붙이고, 지정한 element 앞에 형제 element로 추가

```javascript
function my_func(){
    let my_li_before = $('<li></li>').text('파파고')
    $('ul>li:eq(1)').before(my_li_before)
}
```

