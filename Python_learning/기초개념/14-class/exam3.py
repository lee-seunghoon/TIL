class Helloworld :
    message = 'Python!!'   # <-- 클래스 변수
    
    def setEng(self) :
        self.message = 'Hello Python'  # ---> '인스턴스 변수'
    
    def setKor(self) :
        self.message = '안녕하세요, 파이썬'
        
    def setKor2(self) :
        message = '파이썬 화이팅!'  # ---> 지역변수 (함수안에서 만들어진 변수)
        self.msg = message + ' 아자아자'
        
    def sayHello(self) :
        print(Helloworld.message)
        print(self.message)
        
    def sayHello2(self) :
        print(Helloworld.message)
        print(self.msg)

hello = Helloworld()

'''
hello.setEng()
hello.sayHello()
print('-'*20)

hello.setKor()
hello.sayHello()
print('-'*20)
'''

hello.setKor2()
hello.sayHello2()
print('-'*20)
