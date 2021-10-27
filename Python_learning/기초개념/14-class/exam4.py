# 스태틱 메소드
# => 클래스 밖의 함수를 클래스 안으로 옮겨서 사용하는 방법
# => def 함수명(매개변수) :
#       명령문
# => 사용 : 클래스명.함수명() 

class Calc :
    def plus(self, x, y):
        print('메소드 plus() 호출')
        return x+y
    
    def minus(self, x, y):
        return x-y
    
    def f(self, x, y) :
        result1 = Calc.plus1(x, y)
        result2 = self.plus(x,y)
        result3 = result1 + result2
        return result3
    
    # 아래 함수를 스태틱 메소드라고 함 (함수 안에 self가 없는 것이 차이점 / 클래스 밖에 있는 함수를 가져와서)
    def plus1(x, y) :
        print('스태틱 메소드 plus() 호출')
        return x+y

#스태틱 메소드는 객체 필요 없이 바로 사용 가능

print(Calc.plus1(100,50))
print()
c=Calc()
print(c.plus(100,50))


