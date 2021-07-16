where = input("경기장은 어디입니까? ")
win = input("이긴팀은 어디입니까? ")
lose = input("진 팀은 어디입니까? ")
score = input("스코어는 몇대몇 입니까? ")

# 내가 한거
print()
print("오늘 " + where +"에서 야구경기가 열렸습니다.")
print(win + "과 " + lose + "의 치열한 공방전을 펼쳤습니다.")
print("결국 " + win + "은 " + lose + "를 7:5로 이겼습니다.")
print()

# 선생님이 한거
result = """\
=================================
오늘 %s에서 야구경기가 열렸습니다.
%s과 %s의 치열한 공방전을 펼쳤습니다.
결국 %s은 %s를 %s로 이겼습니다.
=================================
""" %(where, win, lose, win, lose, score)

print(result)

