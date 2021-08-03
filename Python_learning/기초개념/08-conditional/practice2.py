kor = int(input('당신의 국어점수는? '))
eng = int(input('당신의 영어점수는? '))

total = kor + eng
mean = total/2

if mean>=90 :
    score = 'A'
elif mean >=80 :
    score = 'B'
elif mean >=70 :
    score = 'C'
elif mean >=60 :
    score = 'D'
else :
    score = 'F'

print('\n')
print('총점 =', total)
print('평균 =', mean)
print('학점 =', score)


print('''
총점 = %s
평균 = %s
학점 = %s     

축하드립니다. 합격입니다.
''' %(total, mean, score))
