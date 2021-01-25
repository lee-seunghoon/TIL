function my_func() {
    // 없는 element틑 새로 만들고 싶을 때
    let my_div = $('<div></div>').text('소리없는 아우성')

    // 시작하는 tag만 있고, 끝tag가 없는 것을 만들 때는 <input /> 이렇게 사용
    let my_img = $('<img />').attr('src','img/english.jpg')

    // 새롭게 만든 element를 원하는 위치에 붙여야 한다!
    // 4종류의 함수를 이용해서 element를 원하는 위치에 붙일 수 있다.

    // 1.append() : 무조건 자식으로 붙이고, 맨 마지막 자식으로 붙인다.
    let my_li = $('<li></li>').text('아이유')
    $('ul').append(my_li)

    // 2.prepend() : 자식으로 붙이고, 맨 처음 자식으로 붙인다!
    let my_li_pre = $('<li></li>').text('이승훈')
    $('ul').prepend(my_li_pre)

    // 3. after() : 형제로 붙이고, 해당 element 다음 형제 element로 추가
    let my_li_after = $('<li></li>').text('조연')
    $('ul>li:eq(3)').after(my_li_after)

    // 4. before(): 형제로 붙이고, 해당 element 앞에 형제 element로 추가
    let my_li_before = $('<li></li>').text('제니')
    $('ul>li:last').before(my_li_before)
}