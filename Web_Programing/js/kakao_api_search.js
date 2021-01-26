function my_search() {
    let keyword = '영화 포스터 건축학개론'
    let kakao_url = "https://dapi.kakao.com/v2/search/image"
    // let Rest_API = '7a3ed81af7c2aa2be7912bbb20b5f70b'

    // AJAX 방식 활용
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
            alert('성공적으로 호출!')
            let img_url = result['documents'][8]['thumbnail_url'];
            let image = $('<img />').attr('src', img_url);
            $('#myDiv').append(image);

        },
        error : function () {
            alert('뭔가 이상해요')
        }

    })
}