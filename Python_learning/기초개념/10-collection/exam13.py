# 딕셔너리 = {'이름' : 데이터} 
# 딕셔너리 = {'key':value}

dic = {'a':1, 'b':2, 'c':'hello', 'd':'파이썬'}
print(dic)
print('-'*20)


#key(=이름)값 유무 확인

if 'c' in dic :
    print('키 "c"가 존재함')
 
if 'hello' in dic :  # in 연산자는 무조건 키값만 찾는다. 데이터에 있어도 False
    print('키 "c"가 존재함')   
else :
    print('키(key) "hello"가 존재하지 않음 키값으로')

print('-'*20)


# 키(key=이름) 값만 확인 하고 싶을 때
print(dic.keys())


# 데이터(=value)만 확인 하고 싶을 때
print(dic.values())

# key 와 value를 한쌍으로 확인 하고 싶을 때
print(dic.items())

print('-'*20)



# 개별 데이터 확인할 때 조심할 점
# 키값이 없으면 error가 든다.

print(dic.get('a'))  # 키값이 있기 때문에 --> 1
print(dic.get('ff')) # 키값이 없기 때문에 --> None
print('-'*20)

# for문 사용

for key in dic.keys() :
    print(key)

print('-'*20)
    
for val in dic.values() :
    print(val)

print('-'*20)

for item in dic.items() :
    print(item)

print('-'*20)


# 딕셔너리 정렬 시키고 싶을 때

# 키값 기중 오름차순
for key in sorted(dic.keys()):
    print(key, dic[key])    

print('-'*20)

# 키값 기중 내림차순
for key in sorted(dic.keys(), reverse=True):
    print(key, dic[key]) 
print('-'*20)

# 데이터 개수 확인
print(len(dic))
print('-'*20)


# 데이터 추가 : 딕셔너리 형태의 데이터 추가
dic2 = {'e':'빅데이터', 'f':'딥러닝'}
print(dic2)
print('-'*20)


# 딕셔너리 자체를 추가 하기
# 방법1 = 딕셔너리 자체가 같이 들어옴
dic['g'] = dic2
print(dic)
print('-'*20)

# 방법2 = 딕셔너리 안에 키값과 데이터만 데리고 옴
dic.update(dic2)
print(dic)
print('-'*20)





