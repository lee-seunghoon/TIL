'''
아이덴티티 연산자

is = 레퍼런스 변수의 주소값이 같은 지 검사
---> 주소값 같다 : True / 다르다 : False

is not = 레퍼런스 변수의 주소값이 다른 지 검사
---> 주소값 같다 : False / 다르다 : True

id(변수명) : 주소값(레퍼런스 변수) 확인할 수 있다.
'''

a = 1
b = 2
c = 1
d = a

print(a, c, d, sep=', ')
print(b)
print(id(a), id(c), id(d), sep=', ')
print(a is c)
print(a is b)
print(a is d)
print(a is not b)








