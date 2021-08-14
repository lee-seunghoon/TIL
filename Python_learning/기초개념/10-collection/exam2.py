list1=[]
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)

print(list1)


#1~100을 리스트에 저장하기

list2 =[]

# 내가 만든거 .... -----------------
# for list2 in range(1,101):
#     print(list2)


for i in range(1,101):
    list2.append(i) 
print(list2)
    
#리스트에 저장된 데이터의 개수 확인
# len(리스트)

print(len(list1))
print(len(list2))
