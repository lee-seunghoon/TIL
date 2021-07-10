# index = 위치값이 필요하다
# 양수 0123456
# 음수 25242322212019...
st1="abcdefghijklmnopqrstuvwxyz"
print(st1)
print('--------')
print()

# 인덱싱 (indexing)
# --> 문자열에서 문자 1개 확인

# 양수 인덱싱
print(st1[0])
print(st1[2])
print(st1[5])
print(st1[11])
print(st1[25])
print('--------')
print()

#음수 인덱싱
print(st1[-2])
print(st1[-24])
print(st1[-15])
print('--------')
print()

# 슬라이싱 (slicing)
# 문자열에서 부분적으로 문자 여러개 확인
# [시작:끝:step] --> ':step'을 생각하면 step=1을 의미함 / step이란 건너뛰기 값
# 끝 부분 숫자 위치는 빼고 그 앞까지만 반영
print(st1)
print('--------')
print(st1[2:5])
print(st1[0:23])
print(st1[:6])
print(st1[3:])
print(st1[:])
print(st1[2:5:1])
print(st1[2:5:2])
print(st1[2:5:3])
print('--------')
print(st1[::3])
print(st1[::-3])
print('--------')

#문자열 연결하기
st2 = 'xyz'
st3 = st1 + st2
print(st1)
print(st2)
print(st3)
print(st1+st2)
print('--------')

#문자열 반복하기 - 문자열 곱하기를 의미함
st4=st2*3
print("<문자열 반복한 것을 표현한 값>")
print(st4)
print('--------')

#문자의 개수 확인

print("<문자의 개수 확인>")
print(len(st1))
print('--------')

#인덱싱과 슬라이싱으로는 문자를 변경할 수 없음
print(st1)
print(st1[0])
print('--------')
#st1[0]="k" --> error
# 대신 짜집기 해서 바꿀 수 있다.

st1="k" + st1[1:]
print(st1)

st1= st1[:2] + "한글" + st1[4:]
print(st1)
print('--------')
