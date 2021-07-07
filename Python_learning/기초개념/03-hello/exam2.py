print('hello Python')
print(12)
print(5, 7, 9)
print('------')

print(5+7)
print(5.5) 
print(5.7, 6.7, 4.264)
print('------')

#문자열 출력
print("Hello", "Python", '이승훈') 

print('------')

#boolean값 출력
print(True) 
print(True, False, True) 
print('------')     

"""
생각보다 쉽지는 않지만
그래도 재밌는 것 같음
"""

#디버깅의 중요성을 알아야 한다.

#오류 떴을 때 다른 파일은 건들면 안된다. 내가 작업하고 있는 파일만

'''
계산식 gogo
'''

print(2*4)
print(20/100)
print(9+120)
print('------')

#문자열 계산식 (그냥 결합시키네)
print("Hello"+"Python")
print('------')


#숫자와 문자열 합성 ----> 에러난다 아래같이 +로 합성하면
#print(5 + "sh0316") # error
# int =정수 / str = 문자열


#숫자를 문자열로 변환시키면 합성 가능하다
print(str(5) + "sherlock")
print('------')

#다른것도 마찬가지
print(str(True) + "sherlock" )

#서식출력
# --> 서식 문자를 사용해서 출력
'''
%d : 정수, %자리수d
%f : 실수, %자리수.소수점자리수f
%s : 문자열 또는 정수, 실수, %자리수s
'''

print("정수: %d, 실수: %f, 문자열: %s" %(5, 7.7, '홍길동'))
print("정수: %s, 실수: %s, 문자열:%s" %(5, 7.7, '홍길동'))
print("정수: %4d, 실수: %8f, 문자열: %6s" %(5, 7.7, '홍길동'))
print("정수: %4d, 실수: %8.2f, 문자열: %6s" %(5, 7.7, '홍길동'))
print('------')

# sep 속성 (기본값이 공백 1개)
# = 분리문자 속성
print(5, 7.7, 'dltmdgns', True)


print(5, 7.7, 'dltmdgns', True, sep='')
# --> sep는 분리를 나타내서 분리되는 곳을 어떻게 표현하냐.
print(5, 7.7, 'dltmdgns', True, sep=' / ')
print(5, 7.7, 'dltmdgns', True, sep=' + ')
print('------')

# 특수문자 '\n' : 한줄 넘김 문자
print("오늘은\n토요일\n입니다")
print('------')

#end 속성 : 마지막 문자 설정
print("sherlock")
print("holmse")
print('------')

# 위에랑 똑같아 뒤에 end 문자가 있는거야
print("sherlock", end='\n')
print("holmse", end='\n')
print('------')

# 한 줄 넘기지 않고 붙이고 싶을 때는
print("sherlock", end='  ')
print("holmse", end='\n')
print('------')

#나만의 적용 문장
print("1등 점수: %s 이상, 2등 점수: %s, 3등 점수 : %s" %(95.73,87.56,75.657))
print('------')

#변수 --> 데이터를 저장하는 메모리(RAM)상의 공간

#<데이터 저장 방법>
# 변수명(레퍼런스 변수=주소저장) = 데이터 (데이터변수 = 데이터 저장)
# C언어에서는 데이터를 / 자료형 변수명 = 데이터; / 이렇게 표현한다
# C언어 예시 --> int a=5; (=컴퓨터에 정수를 저장하겠다는 명령어)
# RAM 4GB의 의미?? ㅎㅎ --> GB=10의 9승=10억 --> 40억 바이트 -->1비트=8바이트 그러므로 320억 비트
# C언어 간접사용(포인터 변수 = 주소) ---> int*p = %a / p = 7 




