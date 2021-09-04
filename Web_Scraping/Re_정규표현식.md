## 정규표현식(re)

> - 정해진 형태를 의미하는 식 (ex. 주민등록번호, 이메일주소, 차량번호, IP주소)



```python
# 정규식 라이브러리
import re

# 패턴을 만드는데, 우리가 만들 정규식을 컴파일하는 과정
p = re.compile('ca.e') 
# . : 하나의 문자를 의미한다 (ex. ca.e = care, case, cafe (O) | cadgse (X))
# ^ : 문자열의 시작을 의미한다 (ex. ^de = desk, destination (O) | fade (X))
# $ : 문자열의 끝을 의미한다. (ex. se$ = case, base (O) | face (X))

# 내가 만든 정규식과 매칭하는지 확인하는 방법
m = p.match('case')
print(m.group()) # 만약 매칭되지 않으면 에러가 나온다.

# 잘 매칭될 경우, 안 될 경우 구분해서 출력
def print_match(m):    
    if m:
        print(m.group()) # ==> 일치하는 문자열을 반환 (care)
        print(m.string) # ==> 입력받은 문자열을 출력 (good care)
        print(m.start()) # ==> 일치하는 문자열의 시작 index를 출력 (5)
        print(m.end()) # ==> 일치하는 문자열의 끝 index를 출력 (9)
        print(m.span()) # ==> 일치하는 문자열의 시작 & 끝 index를 출력 (5,9)
    else:
        print('매칭되지 않음')

# match는 주어진 문자열에서 처음부터 일치하는지 확인한다 (처음부터 없으면 에러)
m = p.match('careless')
print_match(m) # ==> care 출력

# search : 주어진 문자열 전체에서 일치하는 게 있는지 확인
m = p.search('good care')
print_match(m) # ==> care

# findall : 일치하는 모든 것을 리스트 형태로 반환
lst = p.findall('careless')
print(lst) # ==> ['care']

lst1 = p.findall('good care cafe')
print(lst1) # ==> ['care', 'cafe']

```



> ## 정규식 정리

> 1. p = re.compile('원하는 형태 정규식')
> 2. m = p.match('비교할 문자열') : 주어진 정규식과 비교했을 때, 비교할 문자열의 처음부터 일치하는지 확인
> 3. m = p.search('비교할 문자열') : 주어진 정규식과 비교했을 때, 비교할 문자열 전체에서 일치하는 부분이 있는지
> 4. lst = p.findall('비교할 문자열') : 일치하는 모든 것을 리스트 형태로 출력
> 5. `.` : 하나의 문자를 의미한다 (ex. ca.e = care, case, cafe (O) | cadgse (X))
> 6. `^` : 문자열의 시작을 의미한다 (ex. ^de = desk, destination (O) | fade (X))
> 7. `$` : 문자열의 끝을 의미한다. (ex. se$ = case, base (O) | face (X))



#### `정규식 연습 및 심화 학습 위한 사이트`

- https://www.w3schools.com/python/python_regex.asp
- https://docs.python.org/3/library/re.html



*by. 나도코딩*





