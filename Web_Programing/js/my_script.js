function hello() {
    alert('버튼이 클릭되었어요!!')
    // $ ==> jQuery 사용한다는 의미
    // # ==> id 이용할겁니다.
    // .val() ==> 값을 불러주세요.

    user_key = $('#userKey').val()
    // key = d666cbf6f3b1ff4e48517a6d1b7f3166

    user_date = $('#userDate').val()
    open_api = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'

    my_url = open_api + '?key=' + user_key + '&targetDt=' + user_date

    // 현재 페이지의 url을 바꾸려면 ==> location.href 에 값 주기.
    location.href = my_url

}