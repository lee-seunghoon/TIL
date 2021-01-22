function my_func() {
    // 버튼 누르면 호출되는 함수!
    // jQuery 사용법
    // 1. selector
    //      ==> HTML element를 지칭하는 특수한 표기법을 의미
    // jQuery는 $로 시작한다.!
    // $(selector).method(); ==> selector가 의미하는 element(객체 같은 놈)를 찾겠어

    // 1) 전체 선택자(selector) : *
    // $('*').css('color', 'red'); // ==> jQuery 이용해서 body 안에 있는 모든 element를 다 찾아
                                    // ==> .css() : 스타일을 바꾸는 jQuery 함수
    // 2) 태그 선택자 : 태그명을 가지고 선택
    // $('span').remove();
    // $('li').css('background-color','yellow');

    // 3) ID 선택자 : ID 속성을 이용해서 element를 선택
    //      '#'으로 ID를 찾는다.
    //      .text() ==> 해당 element에 있는 text를 바꾼다.
    // $('#inchon').text('text를 바꿨습니다.');

    // 4) class 선택자 : class 속성을 이용해서 선택
    //    '.'으로 class를 찾는다.
    // $('.region').css('color', 'blue');

    // 5) 구조 선택자 : 부모, 자식, 형제 관계를 이용해서 선택
    //    $( '부모tag > 자식tag' ) ==> 부모 tag에 속해 있는 자식 중 지정한 자식tag만 불러와
    // $('ol > li').css('color', 'red')

    // jQuery를 통해 화면을 제어할 수 있다.
}