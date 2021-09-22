def sumAndMul(a,b):
    tot = a + b
    mul = a * b
    return tot, mul #리턴값이 여러개인 경우는 튜플로 리턴됨

result = sumAndMul(5,7)
print(type(result))
print('''
합 = {}
곱 = {}'''.format(result[0], result[1]))

#unpacking

a,b = sumAndMul(100,200)
print('''
합 = {}
곱 = {}'''.format(a, b))

def sumandmul(a,b) :
    tot = a+b
    mul = a*b
    return tot,mul
