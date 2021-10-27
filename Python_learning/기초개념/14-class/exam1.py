'''
*클래스란..
--> 변수, 함수들의 집합


class 클래스명 :
    맴버변수(=필드, 속성) : 2종류
            1)인스턴스 변수
            2)클래스 변수
    
    맴버함수(=메소드) 2종류
            1)인스턴스 메소드
            2)스태틱 메소드

* 변수의 호칭
a(레퍼런스 변수) = 7(데이터 변수)
b = []
c = 클래스  #클래스를 저장한 레퍼런스 변수를 객체라고 한다.
'''

class Car :
    # 인스턴스 변수 추가 방법1
    # => 함수안에 멤버변수 만들기
    #    self.변수명 = 데이터
    # => 이 함수가 호출되어야만, 실제 변수가 만들어짐
 
    def set(self) :
        self.model = 'E-Class'
        self.color = 'blue'
        self.speed = 10

    def drive(self) :
        self.speed = 20
        
    def output(self) :
        print('모델 :', self.model)
        print('색깔 :', self.color)
        print('속도 :', self.speed)
        

    def output1(self) :
        print('모델 :', self.model)
        print('색깔 :', self.color)
        print('속도 :', self.speed)
        print('메이커 :', self.maker)

mycar = Car()   # <-- 객체 생성 (클래스 사용 준비 완료) 
# mycar. output()   --> 에러 발생, 아직 인스턴스변수가 없기 때문에
print('-'*30)

mycar.set()  # 인스턴스 변수 생성
mycar.output()
print('-'*30)


# self를 쓰지 않고 인스턴스 변수를 쓸 수 있는 방법, 객체.변수명(?) --> 클래스 밖에서 만들 때
print(mycar.model)
print(mycar.color)
print(mycar.speed)    
print('-'*30)

# 인스턴스 변수 추가 방법1
# 객체명으로 만들기
# 주의! --> 이렇게 변수를 만드는 것은 권장하지 않음
mycar.maker = '벤츠' # 클래스 밖에서 만들어졌고, 객체.변수명 --> 인스턴스 변수(함수안에 만들어지는 변수!!

mycar.output1()

