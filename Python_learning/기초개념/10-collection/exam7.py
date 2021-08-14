name = ['홍길동', '김철수', '이영희']
score = [[] for i in range(3)]  # 얘를 2차원 리스트라고 함.
print(name)
print(score) # 얘를 2차원 리스트라고 함. =  [[],[],[]] --> 리스트의 콤마 사이에는 리스트만 존재한다.
# 주의 : 만약 [[],[],10,[]] 중간에 [] 없는 데이터가 들어가 있으면 1차원 리스트!
print()

score[0].append(75)
score[0].append(82)
score[0].append(95)

score[1].append(88)
score[1].append(64)
score[1].append(70)
 
score[2].append(88)
score[2].append(64)
score[2].append(70)

print(score)
print()


# 총점 구하기

tot = [0, 0, 0]

for i in range(3):
    tot[i] = sum(score[i])
    print('%s, 총점=%s 평균=%s' 
          %(name[i], tot[i], tot[i]/len(score[i])))

