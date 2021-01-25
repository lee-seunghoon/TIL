function my_func() {
    // .css()의 치명적인 단점! ==> 다시 rendering한다.
    // 즉, 함수 실행할 때마다, 다시 그림을 그린다.
    // $('div').css('color','red')
    // $('div').css('background-color','yellow')

    // 지정한 tag에 대해서 class를 새로 만들어주는 함수
    // $('div').addClass('myStyle')

    // .removeAttr() ==> 속성을 지울 때!
    $('input[disabled=disabled]').removeAttr('disabled')

    // tag선택자 : div + class선택자 :.myStyle 이렇게 합쳐서 선택가능
    $('div.myStyle').remove()

    // 자신은 삭제하지 말고 자신의 후손들만 모두 삭제!
    // $('div.myStyle').empty()
}
// class 지우는 함수
function remove_func() {
    $('div').removeClass('myStyle')
}