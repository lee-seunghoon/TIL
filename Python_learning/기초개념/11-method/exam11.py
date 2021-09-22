# 함수를 한 줄로 표현하는 람다함수

# 일반 함수

def square1(x) :
    return x**2

def test() :
    print('test')

print(square1(5))
test()
print()


# 람다 함수 유형 1 (명령어가 1개인 함수에만 간단히 적용가능)

square2 = lambda x : x**2
print(square2(5))

test1 = lambda : print('test')
test1()


# 람다 함수 유형 2

a = (lambda x : x**2)(3)
print(a)
print((lambda x : x**2)(3))
(lambda: print('test2'))()

print('-'*30)
print([(lambda x : x**2)(a) for a in range(5)]) # --> 람다 함수를 리스트 내포로... 사용 가능

