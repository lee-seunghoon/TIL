# 논리 연산자
# 집합 기호 --> and(교집합) , or(합집합), not(차집합)
'''
논리 연산자는 수학의 boolean 대수 연산을 명령어로 만든 것이다.

<진리표>
x       y       x and y       x or y      not x
True    True     True         True        False
True    False    False        True        False
False   True     False        True        True
False   False    False        False       True
'''

a=100
b=200
x=5
y=3

r1 = a>=b
r2 = x>=y

print("r1", r1, ", r2=", r2)

r3 = r1 and r2
r4 = r1 or r2
r5 = not r1

print("r3=", r3)
print("r4=", r4)
print("r5=", r5)








