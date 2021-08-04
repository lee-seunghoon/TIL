tot = 0
i = 1

# 조건식 자리에 True를 사용하면
# 조건식을 자유롭게 명령문 사이에 배치 할 수 있음
# 주의 : 이 때 반복문을 탈출할 명령이 있어야 한다.

while True : #true로 하면 무한루프
    if i > 10 : break
    tot += i
    i += 1
    
print(tot)

print('-'*20)

while True : #true로 하면 무한루프
    tot += i
    i += 1
    if i > 10 : break

