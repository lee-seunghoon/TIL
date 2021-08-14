dic = {101:'사과', 102:'복숭아', 103:'감', 104:'바나나'}
print(dic)
print('-'*20)

print(dic.keys())
print(dic.values())
print(dic.items())
# 위에 출력 되는 값들이 리스트는 아니라서 인덱싱이 안된다
print('-'*20)

# 리스트 형태로 변환

list_keys = list(dic.keys())
print(list_keys)
print('-'*20)

print(list_keys[1])
print('-'*20)

list_values = list(dic.values())
list_items = list(dic.items())
print(type(list_values),list_values)
print(type(list_items),list_items)
print('-'*20)

#인덱싱
print(list_keys[2])
print(list_values[1])
print(list_items[0])
print(list_items[0][1])



