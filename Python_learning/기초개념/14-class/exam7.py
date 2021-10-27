class Score :
    def setting(self) :
        print(self)
        self.name = input('이름 : ')
        self.kor = int(input('국어 : '))
        self.eng = int(input('영어 : '))
        self.mat = int(input('수학 : '))
        self.tot = self.kor + self.eng + self.mat
        self.avg = self.tot /3
        
    def output(self) :
        print(self)
        print(self.name, self.kor, self.eng, self.mat,
              self.tot, self.avg)

s1 = Score()
s2 = Score()

print('s1 =', s1)
print('s2 =', s2)
print()

'''
s1.setting()  # s1.set(s1) 이걸 호출하는거나 마찬가지라고 하는데... self값이 s1으로 채워지는..?
print()


s1.output()
'''

