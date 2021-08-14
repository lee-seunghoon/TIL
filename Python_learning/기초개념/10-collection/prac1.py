# 내꺼

student =[]

s1 = int(input('1번 학생의 점수를 입력: '))
s2 = int(input('2번 학생의 점수를 입력: '))
s3 = int(input('3번 학생의 점수를 입력: '))
s4 = int(input('4번 학생의 점수를 입력: '))
s5 = int(input('5번 학생의 점수를 입력: '))

student.append(s1)
student.append(s2)
student.append(s3)
student.append(s4)
student.append(s5)

tot = sum(student)
print()
print('총점 : {}, 평균 : {}'.format(tot, tot/len(student)))


# --------------------------
# 선생님꺼

#입력
jumsu = []
for i in range(5):
    temp = int(input(str(i+1)+"번 학생의 점수를 입력 : "))
    jumsu.append(temp)

#연산
tot = sum(jumsu)
avg = tot/len(jumsu)

#출력
print('총점: {}, 평균: {}'.format(tot,avg))

