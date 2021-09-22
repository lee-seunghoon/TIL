def plus(x,y):
    return x+y

def minus(x,y):
    return x-y


print("100 + 200 = %s" %plus(100,200))
print("100 - 200 = %s" %(minus(100,200)))
print()

a = 5.5
b =7.7

print('{} + {} = {}'.format(a,b,plus(a,b)) )
print('{} - {} = {}'.format(a,b,minus(a,b)) )
