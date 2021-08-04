# for(~하는 동안)
'''
- 횟수 제어 반복 / 정해진 횟수만큼 반복해서 명령문을 수행한다.

=> 데이터가 있는 동안 명령문을 반복 수행하는 명령어

for 변수 in 데이터들 :
    명령문


range 함수
- 정수 만들기 함수
- range(start, end, step)
ex) range(1,5) = 1,2,3,4
    range(5) = 0,1,2,3,4 
    range(1,5,2)
'''

for x in range(9):  #이 때 만들어진 정수 = 0, 1, 2, 3, 4
    print(x)

print()

for x in range(1,5):
    print(x)

print()

for x in range(1,5,2):
    print(x)
    
print()
    
print('-'*20)
print()

for x in 'abcdefg' :
    print(x)

