# 숫자 + 문자열 --> error
# str(숫자)+문자열 --> OK
# str() 함수 = 모든 데이터를 문자열로 변환
# 정수 + 실수 = 실수

num1=5
num2=7.7
d1=True

print(num1,num2,d1,sep=', ')
# print("num1=" +num1)
print("num1= " + str(num1))
print("num1=", num1)
