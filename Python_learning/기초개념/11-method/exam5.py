def total(start, end):
    tot=0
    for x in range(start, end+1):
        tot += x
    return tot

print(total(1,10))
print(total(1,1000000))



