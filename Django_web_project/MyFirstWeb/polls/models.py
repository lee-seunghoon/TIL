from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pud_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text  # ==> 위에 설정한 질문text를 문자열로 표현해주기 위해서!
                                   #     이거 없으면 메모리 주소로 출력됨

    # 여기서 정의되는 class가 데이터베이스의 Table과 mapping 된다!
    # 그럼, Table(pandas dataframe과 동일한 형식)의 column은 어떻게 정의? ==> 속성으로 표현
    # 컬럼명 = models.CharField(max_length=200)
    # models.CharField(max_length=200) ==> 문자열을 의미하는 데 최대 길이 200자로 제한!
    # pud_date = models.DateTimeField('date published') ==> 날짜 형식, 'date published' : 그냥 설명해주는

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

    # models.IntegerField(default=0) ==> 정수 표현, 초기값을 0
    # ForeignKey는 종속의 의미를 갖는다!
    # ForeignKey 제약사항(constraint) : ForeignKey인 원본 data 지우고 싶으면 먼저 ForeignKey와 연결된 table에서 관련 자료 지워야 한다.
    #                                 그런데, 이렇게 하면 너무 복잡하니깐 --> 원본 지우면 링크된 data 같이 지우게 할 수 있다.
    #                                 'on_delete=models.CASCADE' ==> 이렇게 적용!!
