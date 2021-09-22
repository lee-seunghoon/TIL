def grade(s) :    
    
    if s >= 90 :
        return 'A'
    elif s >= 80 :
        return 'B'
    elif s >= 70 :
        return 'C'
    elif s >= 60 :
        return 'D'
    else :
        return 'F'

kor = eng = tot = 0
avg = 0

kor = int(input('국어 점수 입력 : '))
eng = int(input('영어 점수 입력 : '))

tot = kor + eng
avg = tot/2

print(grade(avg), '학점입니다.')