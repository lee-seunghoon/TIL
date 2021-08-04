#구구단 만들기

for a in range(1,10) :
    for b in range(1,10) :
        print('%s*%s=%2s ' %(a,b,a*b), end='')

print('\n')
for b in range(1,10) :
    for a in range(1,10) :
        print('%s*%s=%2s ' %(a,b,a*b), end='')
        