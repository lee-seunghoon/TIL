# *args : 튜플이 전달되고, 그 튜플을 저장함
# => 매개변수에 전달되는 데이터 개수 정해져 있지 않을 때 사용

def total(*args) :
    tot = 0
    for a in args :
        tot += a
    return tot

print(total(1,2))
print(total(1,2,3,4,5))
print(total(10,20,30,40,70,90,100))
