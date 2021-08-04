# 내꺼... 무한 반복

while True :
    a = int(input('몇 단을 출력할 지 입력하시오 : '))
    b=1
    while b<=9 :
        print('%s*%s=%2s' %(a,b,a*b))
        b += 1
        if b ==10 :
            break
    
    if b > 9 :
        c = input('선택하시오(y:계속) : ')
        if c == 'y' : continue
        else :
            print('종료합니다.')
            break

    # c = input('선택하시오(y:계속) : ')
    # if c == 'y' : continue


#쌤꺼 -------------------

# while True :
    
#     #입력
#     dan = int(input('몇 단을 출력할 지 입력하시오 : '))
    
#     #연산, 출력
#     for a in range(1,10) :
#         print("%s * %s = %s" %(dan, a, dan*a))
        
#     b = input('선택하시오(y:계속) : ')
#     if b == 'y' or 'Y' :
#         continue
#     else :
#         print('종료합니다.')
#         break