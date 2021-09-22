'''
def star(n) :
    for a in range(n) :
        print("*", end="")
    print()   #줄넘김
    return    #생략가능

star(1)
star(2)
'''

# 15층 별탑 출력시키기

def star(n) :
    for a in range(n) :
        print('*', end='')
    print()  #줄넘김

for i in range(1,16) :
    star(i)

    