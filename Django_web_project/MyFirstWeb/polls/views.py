from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse

# request는 client의 request를 모아서 객체로 바뀐 것 (django가 자동으로 만들어줌)
def index(request):
    # 데이터베이스를 뒤져서 설문목록을 가져온다.
    # (테이블명 : polls_question , 클래스명 : Question)

    question_list = Question.objects.all().order_by('-pud_date')[:5]
    # 우리가 불러오려는 database의 행 recorde data를 객체로 가져올거야 모두!
    # .oder_by ==> 정령해서 가져 올건데,
    # ('-pub_date') pub_date라는 column을 기준으로, 내림차순으로(마이너스)
    # q_list 안에는 객체 형태로 이뤄진 record가 리스트 안에 쭉 나열된 상태

    context = { 'q_list' : question_list }
    # Data 전달용 dict 생성해서 객체 만들기

    return render(request, 'polls/index.html', context)
    # ==> root templates가 있는데 그 안 html 이름이 index로 똑같으면, root꺼를 먼저 찾는다.
    # ==> 그래서 현재 내 application 안에 templates 속에 내 application 이름과 똑같은 폴더 만들어서
    # ==> 그 안에 index.html 파일 넣어놓은다.

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # ==> 숏컷 함수 : 딱 1개의 객체만 들고오고 없으면 not found 404 에러 출력해!
    # ==> 'pk' : primary key를 의미하고
    #            Question table의 칼럼명 중에서 pk 속성 가지고 있는 값을 가져 온다.
    #            얘도 list형태의 객체로 가져오겠네
    context = {'selected_question': question}
    return render(request, 'polls/detail.html', context)

def vote(request, question_id):
    # view 쪽으로 전달되는 게 '<int:question_id>/vote/'

    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['my_choice'])
        # question.choice_set.get() ==> choice set과 foreign key 연결된 자료 가져올건데
        # pk=request.POST['my_choice']  ==> pk가 request.POST['my_choice']인 것을 가져올건데
        # request.POST == submit 눌렀을 때, <form> tag 안에 있는 url로 POST 방식 요청할 때,
        # 그 아래 선택 돼 있는 name과 value를 쌍으로 넘어옮
        # 예를 들어 name(='my_choice') : value(="{{ choice.id }})" 이게 넘어와
        # 그래서 'my_choice'(name)를 입력하면 이건 value를 즉, choice.id 값을 준다!
        # 그래서 pk 값이 내가 선택한 choice.id 값이다.

    except(KeyError, Choice.DoesNotExist):
        # Key Error 오류가 나면 제외할건데
        # Choice 선택값이 존재하지 않을 때 == 즉, 아무것도 선택하지 않은거야
        # ==> Choice.DoesNotExist

        # 그럼, name : value 이 값이 아무것도 없겠지
        # 그럼, 위 get에서 pk 값을 아무것도 가져올 수 없겠지

        # pk가 없어서 오류가 발생할 경우를 지칭
        return render(request, 'polls/detail.html', {'selected_question': question,
                                                     'error_message': '아무것도 선택하지 않았어요!'})
    else:
        selected_choice.votes += 1
        selected_choice.save()  # ==> 이 객체에 대한 data 내용 변경된거 database에 저장해주세요

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        # HttpResponseRedirect() ==> client에게 url을 보내주고, 그 url로 다시 request해야 원하는 결과 받을 수 있다.
        # reverse() ==> urlconf(urls.py)에 있는 name을 이용해서, url 형식으로 변환시켜준다.
        # reverse('polls:results') ==> polls의 urlconf에서 name이 results인 링크를 줘서 다시 request 하게 한다.
        # 'question_id'에 들어갈 인자로 args 변수 1개 줘야 하는데 '튜플 형식'으로 줘야 한다!
        # 여기서 question은 위에 detail 함수에서 생성했던 question 객체다.

        # HttpResponseRedirect() 와 reverse() 사용하기 위해서는 아래와 같이 import 시켜줘야 한다.
        # from django.http import HttpResponseRedirect
        # from django.urls import reverse


        # context = {'selected_question': question}
        # return render(request, 'polls/detail.html', context)
        # render는 HttpResponse() 이걸 만들어서 client에게 전송해주고, client는 browsing한다.

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
