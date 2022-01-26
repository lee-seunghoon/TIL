'''
import 모듈명 
=> 모듈명.명령어

from 모듈명 import 함수, 클래스
=> 함수명
=> 클래스명
=> 바로 사용 가능
'''

from random import random
from random import randint
from random import randrange
from random import sample

# 0.0 <= 실수 < 1.0 사이의 임의(무작위) 실수값 1개 생성
print(random())
print()
# 0~9 사이의 임의의 정수 생성
print(randint(0,9)) #특이하게 얘는 end값 9까지 다 포함하는 함수...
print()
# 5~10 사이의 임의의 정수 생성
print(randrange(5,10)) # --> step설정 가능
print(randrange(5,10,2)) # --> 5, 7, 9 중에 1개만 랜덤으로 선택 
print()
# 임의 문자 생성 : A~Z = 65~90 / a~z = 97~122  으로 컴퓨터에 설정돼 있음
print(chr(randint(65,90))) #chr 를 통해서 아스키 코드 숫자를 문자로 변경
print(chr(randint(97,122)))
print()
# 리스트에서 임의값을 선택 추출하기
print(sample([1,2,3,4,5],2)) # 리스트 값 중에서 임의의 숫자 2개만 뽑는 것
print()

print(sample([a for a in range(1,46)], 6))

