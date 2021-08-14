# 인덱스 (index : 위치값)
# 양수        0       1      2       3       4
# 음수       -5      -4     -3      -2      -1

str_list = ['국어', '영어', '수학', '사회', '한국사']
print(str_list)
print()

# 인덱싱 : 데이터 1개 사용
print(str_list[1])
print(str_list[3])
print(str_list[-2])
print(str_list[-4])
print()

# 데이터 수정
str_list[0] = '국어2'
print(str_list)
print()

# 슬라이싱 : 데이터 여러개 사용
print(str_list[:4:2])
print(str_list[:4])
print(str_list[1:])
print(str_list[::2])
print(str_list[::-1])
print()

#데이터 검사
if '사회' in str_list : print(str_list.index('영어'))

# for문 이용해서 데이터 1개씩 읽기

for a in str_list :
    print(a)
