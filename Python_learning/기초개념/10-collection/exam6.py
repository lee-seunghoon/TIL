hong = []
hong.append(75)
hong.append(82)
hong.append(95)

kim = []
kim.append(88)
kim.append(64)
kim.append(70)

lee = [100, 95, 90]

print(hong)
print(kim)
print(lee)
print('-'*30)


# 총점 구하기
tot = [0,0,0]

for x in hong :
    tot[0] += x  # = tot[0] = sum(hong)

tot[1] = sum(kim)
tot[2] = sum(lee)

print('홍길동, 총점=%s 평균=%s' %(tot[0], tot[0]/len(hong)))
print('김철수, 총점=%s 평균=%s' %(tot[1], tot[1]/len(kim)))
print('이승훈, 총점=%s 평균=%s' %(tot[0], tot[0]/len(lee)))
