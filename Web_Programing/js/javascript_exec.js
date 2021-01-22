// 1.변수 선언 (파이썬과 거의 비슷)
// 변수 앞에 일반적으로 var이라는 keyword 잡아준다.
// ; ==> 이것의 의미는 ; 여기까지 해당 statement가 종료 됐다!

let tmp1 = 'sample'; // string
let tmp2 = 10;       // number
let tmp3 = true;     // boolean type 소문자로 나타낸다.
let tmp4 = [1,2,3,4] // ==> array

// 출력하고 싶을 때
// alert() 을 이용해서 변수 출력해볼 수 있다.
// consol.log() 또한 이용 가능

// alert(tmp1)  // ==> blocking method : 여기에서 코드의 수행이 일시 중지. (학인버튼 누루기 전까지.

console.log('변수의 값 : ' + tmp1) //

// javascript 객체 (python의 dict와 같은 구조 ==> data 표현 방식은 json으로 return)
let obj = { name : '홍길동',
            age : 25 }

console.log(obj.name)

// 함수 만들기
function add(x,y) {
    return x+y
}

alert(add(10,20))


