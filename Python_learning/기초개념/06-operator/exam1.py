# 연산자 = 수학 기호를 명령어로 만든 것
# 우선순위란 --> 한 줄 명령에 연산자 여러개 나올 때, 어떤 연산자부터 실행할 지 정해 높은 것
# ex) 1+2*3 = 7

# 산술 연산자 1
# + - * / // % **

num1 = int(input("정수 입력 : "))
num2 = int(input("정수 입력 : "))  
          
r1 = num1 + num2

print()
print("<산술연산 예시>")
print(num1, '+', num2, '=', r1)    


r2 = num1 - num2
print(num1, '-', num2, '=', r2) 
r3 = num1 * num2
print(num1, '*', num2, '=', r3) 
r4 = num1 / num2
print(num1, '/', num2, '=', r4)

# 지수 연산자 or 자승 연산자 
r5 = num1 ** 3 
print(num1, '**', 3, '=', r5)

r6= num1 // 2
r7 = num1 % 2
print(r6, r7)
print("""\
      ==================================
      10나누기2 --> 몫은 %s 나머지는 %s
      ==================================
      """ %(r6, r7))


