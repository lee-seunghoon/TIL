def outputNum(nn) :
    print('---출력---')
    for x in range(len(nn)) :
        print(nn[x], end=' ')


def inputNum(nn) :
    for x in range(len(nn)) :
        nn[x] = int(input(str(x+1)+'번째 정수 입력 : '))
                   


print()

n = [0 for x in range(5)]
print(n)

inputNum(n)
print(n)
outputNum(n)




