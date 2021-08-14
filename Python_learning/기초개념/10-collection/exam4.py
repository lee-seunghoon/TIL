a = [1, 2, 3]
print(a)
print()

#인덱싱
a[2] = 100
print(a)
print()

a[1] = ['a', 'b', 'c']
print(a)
print()

print(a[1])
print(a[2])
print()

print(a[1][1]) # 리스트 안에 있는 데이터 중에 리스트 있는 데 그 안에 있는 거 또 가져올 수 있어
print()
print('-'*25)

#슬라이싱
b= [1,2,3]

b[1:2]=['a', 'b', 'c']
print(b)
print()
print('-'*25)

b[1:3] = [100, 200]
print(b)

b[1:4] = [1000]
print(b)
print()

b[1:2] = ['a','d','g','c',100]
print(b)

b[3] = ['a','d','g','c',100]
print(b)



