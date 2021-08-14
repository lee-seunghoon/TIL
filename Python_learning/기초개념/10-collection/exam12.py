# 딕셔너리 = {'이름' : 데이터}  / key값은 문자열과 정수, 실수 가능하다! (bool 값만 안됨)
dic = {'a':1, 'b':2, 'c':'hello', 'd':'파이썬'}
dic1 = {1:1, 2:2, 3:'hello', 4:'파이썬'} # 키값은 정수로 쓸 수 있음


#전체 데이터 확인
print(dic)
print()

#개별 데이터 확인
print(dic['c'])
print(dic['a'])
print()

# 데이터 추가
dic['홍길동']='010-1234-5678'
print(dic)
print()

# 데이터 수정
dic['d']='sherlock'
print(dic)
print()


# 데이터 삭제 : 개별
del(dic['홍길동'])
print(dic)
print()


# 데이터 삭제 : 전체
dic.clear()
print(dic)



