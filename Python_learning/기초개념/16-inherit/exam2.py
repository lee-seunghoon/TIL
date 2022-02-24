'''
다중상속

'''
class CalcParent1 :
    def plus(self, x, y) :
        print('부모 클래스1')
        return x + y
    
    def minus(self, x, y) :
        print('부모 클래스1')
        return x-y

class CalcParent2 :
    def plus2(self, x, y) :
        print('부모 클래스2')
        return x + y
    
    def minus2(self, x, y) :
        print('부모 클래스2')
        return x-y
    
    
class CalcChild(CalcParent1, CalcParent2) :
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
print(calc.plus2(5,7))
print(calc.minus2(5,7))
print(calc.multply(5,7))



    
   
    
   



