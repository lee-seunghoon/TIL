# 인스턴스 함수
# def 함수명(self, 매개변수) :
#    명령문
# => 클래스 안에서 사용 : self.함수명
# => 클래스 밖에서 사용 : 객체명.함수명

class Calc :
    def plus(self, x, y):
        print('메소드 plus() 호출')
        return x+y
    
    def minus(self, x, y):
        return x-y
    
    def f(self, x, y) :
        result1 = plus(x, y)
        result2 = self.plus(x,y)
        result3 = result1 + result2
        return result3
    
def plus(x, y) :
    print('함수 plus() 호출')
    return x+y

c = Calc()  #객체 생성으로 클래스 사용 준비 완료

print('100 + 50 =', c.plus(100,50))  #인스턴스 함수 호출
print()
print('100 + 50 =', plus(100,50))  #일반 함수 호출
print()
print(c.f(100,50))
