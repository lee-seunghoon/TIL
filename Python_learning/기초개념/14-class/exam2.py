# 클래스 변수 : 모든 객체가 공유해서 사용
#       만들기 : 함수밖에서 / 변수명 = 데이터
#       사용법 --> 클래스명.변수명 (객체 생성 없이 바로 쓸 수 있다)
# 인스턴스 변수 : 1개 객체에서만 사용
#       사용법 --> 함수 안 : self.변수명
#       클래스 밖 --> 클래스 밖 : 객체명.변수명

class Car :
    maker = '벤츠'   # => 함수 밖에 있다. = 클래스 변수 
    
    
    def set(self) :  # 인스턴스 변수 = 함수 안에 있다는 의미
        self.model = 'E-Class'
        self.color = 'blue'
        self.speed = 10

    def drive(self) :
        self.speed = 20
        
        

    def output1(self) :
        print('모델 :', self.model)
        print('색깔 :', self.color)
        print('속도 :', self.speed)
        print('메이커 :', self.maker)
        

print('제조사 :' , Car.maker)
print('-'*20)

mycar=Car()
mycar.set()
mycar.output1()

