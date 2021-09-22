'''
지역 변수 
=> 함수 안에 있는 변수
=> 함수 시작시 생기고, 함수 종료시 없어짐

전역 변수 
=> 함수 밖에 있는 변수
=> 프로그램 시작시 생기고, 프로그램 종료시 없어짐

'''

# 전역변수는 모든 함수에서 저장된 내용을 확인할 수 있다.
# but! --> 함수에서 전역변수에 데이터를 저장하기 위해서는 전역변수 선언을 해야한다.
#          global 전역변수명 

def calc_area(radius):
    global area, test1 # <-- area 변수는 전역변수라고 선언하는 행
    print(area)
    print(test)
    print(test1)
    area = 3.14 * radius**2  #원의 넓이 구하는 공식
    test1 = 5*radius
    return area, test1

test = 5
test1 = 15
area = 0

calc_area(5)
