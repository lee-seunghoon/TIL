// ==> 화면에 html 내용이 다 준비되면 그 때! function 시행시켜줘요
// 그냥 바로 이벤트 줄 수는 없다. 왜냐면 html 구동에 순서가 있는데
// 이 javascript jQuery는  밑에 body부분이 읽어지기 전에 먼저 읽어진다.
// 그래서 그냥 h3 찾으라고 하면 아직 안 읽어서 못 찾는다.
// 그래서 .on(ready) 를 부여해줘서 이벤트 가능하게 만들어준다.
$(document).on('ready', function(){
    $('h3').on('click', function(event){
        //alert('클릭되었어요')
        // 이벤트가 발생했을 때 어떤 element에서 event가 발생했는지 판단 파악 필요!
        // 'this'는 현재 이벤트가 발생한 element를 지칭함!
        alert($(this).text())
    })
})

// 위 이벤트의 축약판 (on을 생략하고, ready를 바로 부여)
// $(document).ready(function(){
//     $('h3').on('click', function(event){
//         alert('클릭되었어요')
//     })
// })

function my_func(){
    alert('출력되었어요.')
}

function set_style() {
    $('h1').addClass('myStyle')
}

function release_style() {
    $('h1').removeClass('myStyle')
}

function add_event() {
    // h2을 찾아서 이벤트 처리할 수 있는 능력을 부여해주는 함수!!
    // 이벤트발생 함수 ==> .on('어떤이벤트?', '저 이벤트 시행됐을 때, 어떤 기능 수행?')
    // function( 앞에 시행한 이벤트 객체가 전달된다. )
    $('h2').on('click', function(event){
        alert('h2가 클릭되었어요.')
    })
}