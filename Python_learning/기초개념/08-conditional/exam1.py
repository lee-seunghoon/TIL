# 제어문
'''
1. 조건문
=> if

2. 반복문
=> for, while

3. 기타 : 단독으로 사용할 수 없음
=> break, continue, else
'''

# 블럭(Block) = 명령어들을 묶는 단위
'''
-c언어, 자바
{
      명령어
      명령어
 }

-파이썬
 =>  콜론(:)이 블럭의 시작이고,
     들여쓰기(indent)로 같은 블럭을 표현함
     반드시 세로줄이 일치해야함.
     세로줄이 다른 경우 같은 블럭으로 인식하지 않음
     
 조건문 또는 함수명 또는 클래스명 :
         명령문
         명령문
         명령문
'''


# 조건문 = if
'''
조건식이 참이면 명령어를 실행
조건식이 거짓이면 명령어를 실행하지 않음

1) 기본모양 
if 조건식(or 변수) :
    명령문
    
2) 모양2
if조건식(or 변수) : 명령문 (=명령어 한 개 일때만 이렇게 사용 가능)
'''


score = int(input("점수 입력 : "))
if score >=90 and score <=100 :
    print("A학점 입니다")
if score >=80 and score <90 :
    print("B학점 입니다")
if score >=70 and score <80 :
    print("C학점 입니다")
if score >=60 and score <70 :
    print("D학점 입니다")
if score >=0 and score <60 :
    print("F학점 입니다")
print('-'*20, end='\n'*2)






