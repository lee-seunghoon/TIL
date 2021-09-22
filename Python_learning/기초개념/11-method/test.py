'''
f(x) = 2x + 1

x는 매개변수( = 전달된 데이터를 저장하는 변수)

return : 되돌아가라, 호출된 곳으로 되돌아가라.

return 옆에 있는 값은 결과값=리터값 이라 한다.
'''

def f(x) :
    return 2*x + 1

result = f(5)  # f(5) <-- 함수의 호출 : 함수의 사용
print(result)
print(f(2))
print(f(3))
print()

