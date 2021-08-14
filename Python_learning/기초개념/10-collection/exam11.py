tup1 = (1,2.89037120,3,4,5)

# 서식 지정 출력 : 서식 문자 사용
print('%s %s %s %s' %(tup1[0],tup1[1],tup1[2],tup1[3]))

# 서식 지정 출력 : format() 함수 사용
# '문자열'.format(데이터)
print('{} {} {} {}'.format(tup1[0],tup1[1],tup1[2],tup1[3]))
print('{3} {1} {0} {2}'.format(tup1[0],tup1[1],tup1[2],tup1[3]))
print('{} {} {} {}'.format(*tup1)) #이건 tup1 안에 있는 데이터 순서대로 다 불러옴 편하네
print('{4} {1} {2} {0}'.format(*tup1))

tup2 = [1,2,3,4,5]

print('{4} {1} {2} {0}'.format(*tup2))


print('{1:.3f}'.format(*tup1)) 
# 리스트나 변수 안에 있는 데이터 중 소수점 자리수 지정해서 출력하는 방법


# 튜플 unpacking도 리스트와 똑같음

# unpacking : 리스트나 튜플에 저장된 데이터를 개별 변수에 저장하는 것
# but 주의 : 개별변수의 갯수와 리스트의 데이터 갯수가 일치해야 한다.

#upacking
list1 = (10, 20 ,30)
a, b, c = list1
print(list1)
print(a, b, c)

a,b = list1[:2]
print(a,b)
print(a)
print()