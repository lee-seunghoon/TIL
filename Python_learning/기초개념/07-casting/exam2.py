'''
bool(변수 or 데이터 직접) : 데이터 있는지 없는지 True False로 구별
=> True : 데이터 있음
=> False : 데이터 없음
'''

print(bool(0)) # 초기값
print('-'*20)

# 실수
print(bool(5.5))
print(bool(0.0)) # 초기값
print('-'*20)

# 문자열
print(bool('abcd'))
print(bool(''))
print(bool(' ')) # 공백문자는 문자이기 때문에 Ture
print('-'*20)

a = None
print(bool(a))
print('-'*20)

print(a, type(a))
