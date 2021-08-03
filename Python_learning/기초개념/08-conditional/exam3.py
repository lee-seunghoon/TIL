# 

year = int(input('년도 입력 : '))

# if(4의 배수 검사) (100의 배수가 아닌지 검사) (400의 배수인지 검사)
'''
4의 배수 검사 --> 
'''

# and가 or보다 우선순위가 빠르다
if (year%4==0) and (year%100 !=0) or (year%400==0) :
    print(str(year) + "년은 윤년입니다.")
else :
    print(str(year) + "년은 평년입니다.")
    