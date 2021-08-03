s1 = float(input('첫 번째 수 = '))
s2 = float(input('두 번째 수 = '))
s3 = input('연산 부호는?(+,-,*,/ 만 입력해주세요) ')

if s3 == '*' :
    result = s1*s2
elif s3 == '+' :
    result = s1+s2
elif s3 == '-' :
    result = s1-s2
elif s3 == '/' :
    result = s1/s2
else :
    result = None

print('\n')
print(s1, s3, s2, '=', result)


