# 로또 번호 만들기

from random import sample

class Lotto :
    def __init__(self): # 내가 클래스에서 사용 할 인스턴스 변수들을 여기에 만들어놓고 바로 사용
        self.m = 0      # 로또번호 1세트 저장
        self.buyNum = 0 # 구매 회수
        
    #구매회수 입력
    def inputBuyNum(self):
        self.buyNum = int(input('구매횟수를 입력해주세요: '))
        print()
        
    def outputResult(self):
        for i in self.m :
            print('%2d ' %i, end='')
        print()
    
    def selectLotto(self):
        for i in range(self.buyNum):
            self.m = sample([a for a in range(1,46)],6) # 임의숫자 6개 추출
            self.m.sort() # 임의 숫자 6개 오름차순 정렬
            self.outputResult()
            
lotto = Lotto()
lotto.inputBuyNum()
lotto.selectLotto()
