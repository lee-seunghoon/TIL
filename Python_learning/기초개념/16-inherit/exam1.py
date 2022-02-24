'''
* 상속
- 클래스의 결합 방법
- 장점 : 기존 클래스를 건드리지 않고, 기존 클래스에 기능을 추가하거나 수정할 수 있다.
- 메소드의 오버라이딩(덮어쓰기)
  부모 클래스와 자실 클래스에 똑같은 이름의 메소드 존재할 경우, 무조건 자식 클래스의 메소드가 동작됨
'''

class CalcParent :
    def plus(self, x, y) :
        print('부모 클래스')
        return x + y
    
    def minus(self, x, y) :
        print('부모 클래스')
        return x-y
    
class CalcChild(CalcParent) :
    def multply(self, a, b) :
        print('자식클래스')
        return a*b
    
    def plus(self, x, y) :
        super().plus(x,y)   # --> 부모 클래스의 함수를 호출한다.
        print('덮어쓰기 한 자식클래스')
        return x**2 + y
    
calc = CalcChild()

print(calc.plus(5,7))
print(calc.minus(5,7))
print(calc.multply(5,7))
