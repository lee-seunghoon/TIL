class Car : 
    def __init__(self, speed=0, color='blue', model='E-class') : #매개변수에 디폴트값 설정 가능
        print('--생성자 호출 --')
        self.speed = speed  #인스턴스 변수
        self.color = color
        self.model = model
    
    def output(self) :
        print('속도 :', self.speed)
        print('색상 :', self.color)
        print('모델 :', self.model)
    
myCar = Car() # myCar.__init__()
myCar.output()
print('-'*30)

myCar1 = Car(10) # myCar.__init__(10)
myCar1.output()
print('-'*30)

myCar2 = Car(100,model='S-Class')
myCar2.output()
print('-'*30)

myCar3 = Car(100,model='S-Class')
myCar3.output()
myCar3.__init__(50, 'yellow', 'C-Class')
myCar3.output()
print('-'*30)

