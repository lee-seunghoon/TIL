# if else
'''
1.
if 조건식 :
    명령문 
else :
    명령문 
    
2.
if 조건식 : 명령문
else : 명령문
'''

num1 = int(input('첫번째 정수 입력 : '))
num2 = int(input('두번째 정수 입력 : '))


if num2 > num1 :
    num1, num2 = num2, num1
else :
    num1, num2 = True, False

print('큰 값 : %s, 작은 값 : %s' %(num1, num2))


