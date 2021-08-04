# 내꺼------------------------------------
a=0

for a in range(1,101):
    if a%7 == 0 :
        print(a)

print('-'*30)

# 쌤꺼------------------------------------

num1 = int(input('1~100 사이의 배수를 구할 숫자 입력 : '))
s1 = 0

for a in range(1,101):
    if(a%num1 == 0) :
        print(a, end=' ')
        s1 +=1

print()
print('1~100 사이의 %s의 배수 개수 = %s' %(num1, s1))
