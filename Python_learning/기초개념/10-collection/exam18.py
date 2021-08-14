a = [1,2,3,4,5]
b = (6,7,8,9,10)
c = {11,12,13}


print(type(a),a)
print(type(b),b)
print(type(c),c)
print()

# 리스트를 세트와 튜플로 변환

s1 = set(a)
t1 = tuple(a)
print(type(s1),s1)
print(type(t1),t1)
print()

# 튜플을 세트와 리스트로 변환
s2 = set(b)
l2 = list(b)
print(type(s2),s2)
print(type(l2),l2)
print()

# 세트를 리스트와 튜플로 변환
l3 = list(c)
t3 = tuple(c)
print(type(l3),l3)
print(type(t3),t3)
print()

