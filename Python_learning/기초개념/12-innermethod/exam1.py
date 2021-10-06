score =[]

for i in range(4):
    score.append(int(input(str(i+1)+'번째 점수를 입력하세요. ')))

print(score)

#score = [70,80,90,87]

tot = sum(score)
num = len(score)
avg = tot/num
maxScore = max(score)
minScore = min(score)

print('score :', score)
print('총점 : {}, 평균 : {:.1f}'.format(tot, avg))
print('최고점수 : {}, 최저점수 : {}'.format(maxScore, minScore))
