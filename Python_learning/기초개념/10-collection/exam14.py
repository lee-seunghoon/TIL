dic = {'a' : 1, 'b':2, 'c':'hello', 'd':'파이썬'}
print(dic)
print('-'*20)

print('{} {} {} {}'.format(*dic))
print('{0} {1} {2} {3}'.format(*dic))
print('{a} {b} {c} {d}'.format(**dic))
print('{}:{a}, {}:{b}, {}:{c}, {}:{d}'
      .format(*dic, **dic))


