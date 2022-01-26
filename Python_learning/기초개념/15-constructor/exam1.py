'''
* 클래스의 동작 원리
1. self 
=> 어떤 객체가 인스턴스 변수와 인스턴스 메소드를 사용하는 지 구분하는 구분자이다.

2. 생성자 (__init__)
=> 무조건!! 객체 생성시 자동 호출 되어지는 메소드(함수)!
=> 용도 : 인스턴스 변수 설정 및 초기화
=> 초기화 : 변수에 우리가 원하는 데이터를 처음 저장하는 것
'''

class Car : 
    # (speed, color, model) --> 얘네는 지역변수다!
    def __init__(self, speed, color, model) :
        print('--생성자 호출 --')
        self.speed = speed  #인스턴스 변수
        self.color = color
        self.model = model
        
myCar = Car(0, 'blue', 'E-class') # myCar.__init__(0, 'blue', 'E-class') 이게 자동으로 호출되면서 인스턴스 변수가 만들어짐. (따로 호출이 필요없어)

print(myCar.speed)
print(myCar.color)
print(myCar.model)

