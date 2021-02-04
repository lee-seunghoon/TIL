
document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {

        headerToolbar: {

            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth'
        },
        // plugins: [googleCalendarPlugin, interaction, core, moment, daygrid],
        buttonText: { //버튼 글자 커스텀
            today: '오늘',
            month: '월'
        },
        selectable: true,
        // plugins: [ dayGridPlugin, interactionPlugin ],
        // themeSystem: 'bootstrap',  // <== 부트스트랩 테마 적용
        editable: false,
        unselectAuto: true,
        locale: 'ko',
        timeZone: 'Seoul/Asia',
        defaultAllDay: false,

        // googleCalendarApiKey: 'input your key',



        eventSources: [
            // {
            // googleCalendarId: 'ko.south_korea#holiday@group.v.calendar.google.com'
            // },
            // {
            //     googleCalendarId: 'input your id',
            //
            // },
            {
                events: [
                    {
                        title: 'Test1',
                        start: '2021-02-03 06:00',
                        id: 'test',
                        groupId: 'same',
                        allDay: true,

                        // color: 'yellowgreen',
                        backgroundColor: 'red',
                        borderColor: 'yellow',
                        startEditable: true,
                        durationEditable: true,


                    },
                    {
                        title: '프로젝트 종료',
                        start: '2021-02-16 15:30',
                        end: '2021-02-18',
                        // daysOfWeek: ['1'],  // ==> 주간 반복
                        allDay: false,
                        overlap: false  // ==> 일정끼지 겹칠 수 없음


                        // startTime: '14:00',  // ==> 시작시간을 설정하는데 자동으로 everyday 반복 설정
                        // endTime: '18:00'     // ==> 끝나는 시간 설정, 마찬가지로 자동 반복 설정 됨.

                    }
                ]
            }
            ],
        eventDidMount: function() {
            console.log(calendar.getEvents()[0].title);
            // 콘솔창에 evets중 제일 첫번째 있는 객체에서 title 값인 'Test1'을 출력
        },
        dateClick: function(info) {
            alert('Date: ' + info.end);
            alert('Resource ID: ' + info.resource.id);
        },
        select: function (info) {
            var title = prompt('새로 생성할 이벤트 : ');
            if(title){
                calendar.addEvent({
                    title : title,
                    start : info.start,
                    end: info.end,
                    allDay: true
                })
            }
            // calendar.unselect()
            // alert('선택된 날짜' + info.startStr + '~' + info.endStr)
        },
        eventClick: function(info) {  // ==> 클릭했을 때 새로운 event 발생
            alert('Event : ' + info.event.title );

            let new_title = prompt('내용을 수정하시겠습니까?');
            let new_start = prompt('수정하고싶은 시작날짜 입렵해주세요.')
            let new_end = prompt('수정할 끝 날짜를 입력해주세요.')
            if (new_title) {
                info.event.setProp('title', new_title)  // ==> 날짜 외 속성들 값 바꾸는 방법
                // info.event.setAllDay(true) // ==> allday true 주는 방법
                info.event.setProp('backgroundColor', 'green')  // 배경(bar)색깔 바꿔주는!
                info.event.setProp('borderColor', 'red') // ==> 테두리 바꿔주는!

                // event.setDates( start, end, { 'allDay : true or false } )
                // info.event.setDates(moment(info.event.start).days(24).toDate(), moment(info.event.start).days(24).toDate(), {'allDay': false}) // ==> 날짜 이동하는 방법
                info.event.setDates(new_start, new_end, {'allDay': true})
            }

            // alert('새로 바뀐 제목 ==> ' + info.event.title);
            // alert('Coordinates : ' + info.jsEvent.pageX + ',' + info.jsEvent.pageY);
            // alert('View : ' + info.view.type);
        },

        eventResize: function(info) {
            if (confirm('수정하시겠습니까?')) {
                var msg = updateFunc(info);
                alert(msg);
            }
            else {
                info.revert()  // 취소 시키기 (원래 상태로 되돌리기) <== 없을 경우 무조건 이동이 이뤄짐
            }
        }

    });


    calendar.render();

});


