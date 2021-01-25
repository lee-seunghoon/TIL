function my_func() {
    console.log($('#apple').text()) // ==> tag 사이에 있는 글자 가지고 오고 싶을 때 : .text()
                                    // ==> console.log : console 창에 출력
    $('#pineapple').text('이 글자로 대체') // ==> .text() 안에 인자가 있으면 그 글자로 대체

    console.log($('ul > .mylist').text())

    console.log($('#uId').val()) // ==> 입력박스 상자 안에 있는 값을 가져올 때는 val() 사용!

    console.log($('input[type=text]').attr('id')) // ==> 속성 값을 알아내는 함수 : .attr()
    $('input[type=text]').attr('size', 30) // ==> 해당 속성의 값을 바꿀 수 있다.

    console.log($('ol>li:first').text()) // ==> 첫번째, li 값 가져오기
    console.log($('ol>li:last').text()) //  ==> 마지막, li 값 가져오기

    console.log($('ol>li:first+li').text()) // ==> 2번째 li tag값 가져오기

    console.log($('ol > li:eq(1)').text()) // ==> eq는 순번을 지정해주는 selector (index같은)

    // 여러개 찾은 다음에 각각 출력하려면?
    // each하면 index 값이랑, element 한개 자체를 가져온다.
    // 그래서 ol 자손중 li tag들 하나씩 반복해서 가져올건데
    // idx == index / item == 하나의 tag 전체 element
    // 그래서 1 tag에 대해 jQuery 한 번 더 적용해줘야 해

    $('ol > li').each(function(idx,item) {
      console.log((idx+1) + '번째 ' + $(item).text() + '입니다.')
    })
}

// 명시적 함수
// 함수에 이름이 있다
// 그런데 이름이 없는 함수를 만들 수 있다.

// 묵시적 함수 (==lambda 함수)
// 이런 묵시적 함수는 독립적으로 선언하지 못하고 변수에 담아서 사용한다.
// 즉, 함수를 어떻게 취급하냐면 ==> 함수를 하나의 값으로 인식한다! ==> first class
// 그래서 이 묵시적 함수는 하나의 값으로 인식되기 때문에 다른 함수의 인자로 사용할 수 있다.

let kaka = function() {}