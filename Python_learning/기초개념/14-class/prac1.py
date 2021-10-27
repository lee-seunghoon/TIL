class Triangle :
    def setTriangle(self,x,y) :
        self.x = x
        self.y = y
    
    def getArea(self) :
        return self.x * self.y / 2

print('***** 삼각형 넓이 구하기 *****')
b = int(input('밑변 : '))
h = int(input('높이 : '))

t = Triangle()
t.setTriangle(b,h)

print('삼각형의 넓이 :', t.getArea())

# -----------------------------------

