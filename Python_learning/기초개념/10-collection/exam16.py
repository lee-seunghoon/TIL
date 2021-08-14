# 세트는 중복 데이터 허용 X
# 세트는 index가 없음
# 세트는 개별 데이터를 확인할 수 없다.
# but 개별 데이터는 사용하기 위해서는 리스트로 변환해서 사용
# or for문 사용

a= [1,2,3,1,2,3]
print(a)
print(len(a))
print()

b= {1,2,3,1,2,3}
print(b)
print(len(b))
print()

# set 자료로 바꾸기

c = set(a)
print(c)
print()

# 데이터 추가
b.add(4)
print(b)
print(len(b))
print()

#개별 데이터 뽑아보자

for v in b:
    print(v)
    

# 정렬이 가능할까?

print(sorted(b)) # 정렬되면서 리스트형으로 바꿔서 인덱스랑 다 됨
sh = sorted(b, reverse=True)
print(sh[0])
print()

# 데이터 수정은 안된다..

# 데이터 삭제 고고
print(b)
print()
b.remove(4)
print(b)
print()

# 모든 데이터 삭제
b.clear()
print(b)
print()

d = {}  # <-- 이 아이는 비어 있는 딕셔너리
e = set()  # <-- 이 아이는 비어 있는 세트

print(type(d),d)
print(type(e),e)
print()












