# 다중 if-else문 : elif ---> 다중선택 시 사용

'''
모양(1)
if 조건식 :
    명령문
else :
    if 조건식 :
        명령문
    else :
        if 조건식 :
            명령문
        else :
            명령문

모양(2) ★ else와 if 사이에 또 다른 명령문이 온다면 이걸 쓸 수 없다는데...
if 조건식 :
    명령문
elif 조건식 :
    명령문
elif 조건식 :
    명령문
else :
    명령문
'''


score = int(input("점수 입력 : "))

if score >=90 :
    print("A학점 입니다")
elif score >=80 :
    print("B학점 입니다")
elif score >=70 :
    print("C학점 입니다")
elif score >=60 :
    print("D학점 입니다")
elif score >=0 :
    print("F학점 입니다")
print('-'*20, end='\n'*2)
