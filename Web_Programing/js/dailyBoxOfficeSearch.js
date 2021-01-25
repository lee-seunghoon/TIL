function my_func(){
    // 사용자가 입력한 날짜를 가져와서
    // 해당 날짜에 대한 boxoffice 순위를 알려주는
    // 서버쪽 웹 프로그램을 호출하고
    // 그 결과를 화면에 출력

    let user_date = $('#userInputData').val()
    let user_key = 'd666cbf6f3b1ff4e48517a6d1b7f3166'
    let open_api = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
    // let my_url = open_api + '?key=' + user_key + '&targetDt=' + user_date
    //
    // location.href = my_url
    // ==> 이렇게 하면 화면 refresh가 일어나서 원하는 작업을 할 수 없다.

    // 이 문제를 해결하기 위해
    // JavaScript가 가지고 있는 특별한 통신방식을 이용!!
    // ==> 이것이 바로 AJAX

    // 순수 Javascript의 AJAX 코드 구현이 너무 어렵고 힘들어서
    // jQuery 이용할 예정!

    // jQuery가 가진 기능 중에 ajax를 이용할 때 사용 문법
    // javascript의 객체인 '{key : value}' 이용
    // url == 내가 호출할 서버쪽 프로그램 입력
    // type == 호출을 어떤 방식으로 할거냐? (get or post)
    // dataType == 결과 data가 어떤 형태로 오느냐 (csv, xml, json ??)
    // data == 서버에 넘겨줘야 할 data
    // 넘겨중 데이터가 2개여서 value 쪽에 또다시 javascript 객체 부여

    $.ajax({
        url : open_api,
        type : 'GET',
        dataType : 'json',
        data : {
            key : user_key,
            targetDt : user_date
        },
        success : function() {
            alert('서버 호출 성공')
        },
        error : function () {
            alert('뭔가 이상해요!')
        }
    })

}