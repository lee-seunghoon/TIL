# 파일 열기
f = open('test.txt', 'w') # --> 쓰기모드로 이 파일 열었다.

# 파일에 데이터 저장 (데이터는 무조건 문자열로만 저장 가능하다!)
f.write('데이터 출력\n')
#f.write(5)
#f.write(7.7)
#f.write(True)

for i in range(1,11) :
    f.write(str(i+1)+'번째 줄입니다.\n')

# 파일 닫기
f.close()
print('쓰기 완료')
