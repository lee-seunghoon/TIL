# 람다함수의 용도 : 1줄 명령어를 따로 분지하지 않고 1번만 사용!
# 람다함수가 일반 함수보다 속도가 훨씬 빠르다.

a= (lambda x,y,z :x + 2*y + 5*z)(1,2,3)
print(a)


#일반 함수로는 이렇게 길게 만들어야 함
def fomula(x,y,z):
    result = x + 2*y + 5*z
    return result

print(fomula(y=2, z=3, x=1))
