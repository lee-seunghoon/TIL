# with 문을 사용한 파일 읽고 쓰기

# 파일 쓰기
with open('test4.txt', 'w') as f :
    f.write('이걸로 새롭게 저장하는것인가')
    print('저장완료')


# 파일 읽기
with open('test4.txt', 'r') as f :
    text = f.read()
    print(text)

