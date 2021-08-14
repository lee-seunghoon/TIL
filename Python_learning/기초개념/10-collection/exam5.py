# CRUD
'''
대량의 데이터를 처리하는 기본 기능을 나타냄
C : creat = 저장
R : read = 읽기
U : update = 수정
D : delet = 삭제
'''

str_list = ['국어', '영어', '수학', '사회', '한국사']
print(str_list)
print()

# 항목 변경 : 인덱싱
str_list[3] = '과학'

# 항목 추가 : 제일 뒤에
str_list.append('세계사')
print(str_list)
print()

# 중간에 항목 추가
str_list.insert(2, '일본어')
print(str_list)
print()


# 데이터 정렬하기(sort) (원본 데이터는 순서가 안 바뀜)
print(sorted(str_list)) # 함수를 활용해서, 오름차순 정렬
print()
print(sorted(str_list, reverse=True)) # 내림차순 정렬
print()

# 데이터 정렬하기(sort) (원본 데이터 순서가 바뀜)
str_list.sort()
print(str_list) #오름차순
print()

str_list.sort(reverse=True)
print(str_list) #내름차순
print()


# 데이터 삭제 1 : 인덱싱과 슬라이싱으로 삭제
del(str_list[4])
print(str_list)
print()

del(str_list[0:2])
print(str_list)
print()


# 데이터 삭제 2 : 데이터로 삭제
if '영어' in str_list :
    str_list.remove('영어')
print(str_list)
print()

# 모든 데이터 삭제
str_list.clear()
print(str_list)
print()

print(str_list.count())






