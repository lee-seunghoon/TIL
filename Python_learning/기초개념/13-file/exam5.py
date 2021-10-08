'''
파일 포맷

1. csv ---> 단점 : 데이터를 한 눈에 파악하기 어렵다 / 장점 : 용량이 적다
형식
kor,eng,mat
90,80,70
100,90,80


2. xml ---> 단점 : 글이 많다   / 장점 : 데이터 파악 쉽다
<students>  #시작태그
        <students>
                <kor>90</kor>
                <eng>80</eng>        
                <mat>70</mat>
        </students>
        <students>
                <kor>100</kor>
                <eng>90</eng>        
                <mat>80</mat>
        </students>
</students> # 끝 태그

3. json ---> csv와 xml 절충
{
     {kor:90, eng:80, mat:70}, 
     {kor:100, eng:90, mat:80}
}
'''


students = []

with open('test.csv', 'r', encoding='utf-8') as f :
    lines = f.readlines()
    print(lines)
    
    #전처리 작업 : 데이터를 사용하기 편하게 가공하는 것
    for line in lines :
        line = line.replace('\n', '') # '\n' 문자 제거
        print(line)
        line = line.split(',') # ',' 기준으로 문자 분리
        print(line)
        students.append(line)

print(students)


# 성적 처리
result = '' #for문 안에 있는 result는 지역변수여서 전역변수 하나 만들어줘야 \+= 적용이 가능함
for student in students :
    name, kor, eng, mat = student # list 자료 unpacking으로 처리
    tot = int(kor) + int(eng) + int(mat)
    avg = tot/3
    result +='이름: {}, 국어: {}, 영어: {}, 수학: {}, 총점: {}, \
평균: {:.1f}\n'.format(name, kor, eng, mat, tot, avg)
    
print(result)    
#파일 저장
with open('result.txt', 'w') as f :
    f.write(result)




        
    



