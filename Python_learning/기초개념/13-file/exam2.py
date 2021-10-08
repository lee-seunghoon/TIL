# 방법1

#파일 열기
fname = input('파일 이름을 입력하세요.')
f=open(fname, 'r')

#파일 읽기

text = f.read() # 통째로 문자를 읽어옴
print(text)
t1 = text.split('\n')
print(t1)

#파일 닫기
f.close
print('-'*30)

'''
# 방법2
f= open('test.txt', 'r')
while True :
    line = f.readline() # 1줄씩 읽어옴
    if not line : break
    print(line, end='')
f.close()
print('-'*30)

# 방법3
f= open('test.txt', 'r')
lines = f.readlines() # 전체를 1줄씨, 리스트로 저장후 리턴함 / 즉, 위 방법1에서 read와 split을 혼합한것과 마찬가지
print(lines)
f.close()
print('-'*30)


# 궁금증
f= open('test.txt', 'r')
line = f.readline()
print(line)
f.close()
'''

