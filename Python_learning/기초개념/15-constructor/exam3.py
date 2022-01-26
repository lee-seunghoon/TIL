class Car : 
    def __init__(self, speed=0, color='blue', model='E-class', maker = 'Benz') : #매개변수에 디폴트값 설정 가능
        print('--생성자 호출 --')
        self.speed = speed  #인스턴스 변수
        self.color = color
        self.model = model
        self.__maker = maker  # 이렇게 프라이빗하게 설정된 변수는 클래스 안에서만 사용 가능
    
    def output(self) :
        print('속도 :', self.speed)
        print('색상 :', self.color)
        print('모델 :', self.model)
        print('브랜드 :', self.__maker)
    '''    
    def getMaker(self) :  
        # 프라이빗으로 설정된 변수값 확인 : getter --> get+변수명
        return self.__maker
    
    def setMaker(self, maker) : # 프라이빗으로 설정된 변수에 값 저장
        self.__maker = maker
    '''    
myCar = Car(100,'red','S-class')
myCar.output()
print('-'*30)
'''
print(myCar.model)
print('-'*30)

# print(myCar.__maker)  --> 클래스 밖에서 사용할 수 없어

#getter 사용 후 가능
print()
myCar.speed = 50
myCar.setMaker('Audie')
print(myCar.getMaker)
myCar.output()
print('-'*30)
'''
