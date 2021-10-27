# 다른 파일에 있는 클래스를 사용하기 위해서는
# 파일을 포함시켜야 한다.
# 첫번째 방법 - import 파일명
# 두번째 방법 - from 파일명 import 클래스명

# 1) import 파일명
import calculator
c = calculator.Calc()
print(c.plus(100,50))
print(c.minus(100,50))

# 2) from 파일명 import 클래스명
from calculator import Calc
c= Calc()
print(c.plus(100,50))
print(c.minus(100,50))

# 3) from 파일명 import 클래스명 as 별명   
from calculator import Calc as calc
c= calc()
print(c.plus(100,50))
print(c.minus(100,50))


    