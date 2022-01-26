class Car : 
    def __init__(self, speed=0, color='blue', model='E-class') :
        print('--생성자 호출 --')
        print('init함수는 왜 출력 되는거지??')
        self.speed = speed  #인스턴스 변수
        self.color = color
        self.model = model
    
    def output(self) :
        print('속도 :', self.speed)
        print('색상 :', self.color)
        print('모델 :', self.model)
    
    # 객체명을 출력하면 자동호출되는 메소드 
    # --> 인스턴스 변수값을 확인하는 용도로 사용
    def __str__(self) :
        print('-- __str__() 호출 --')
        result = '속도 : ' + str(self.speed) + '\n색상 : ' + self.color + '\n모델 : ' + self.model
        return result            
'''
myCar = Car()
myCar.output()

print(myCar) # --> myCar.__str__() 이 함수를 자동 호출
print(myCar.__str__())
'''

car = Car()

print(car)

