
class Triangle :
    def __init__(self, m, n) :
        self.m = m
        self.n = n
        Area = self.m * self.n / 2
        self.__Area = Area

    
    def getArea(self):
        return self.__Area
        
    def setTriangle(self, Area) :
        self.__Area = Area
        
t1 = Triangle(45,7)
print('삼각형의 넓이 :', t1.getArea())       



# ------------------- 선생님꺼 시작 ------------------------
'''
class Triangle :
    def __init__(self, m=0, n=0) :
        self.base = m
        self.height = n
        
    
    def setTriangle(self, m, n) :
        self.base = m
        self.height = n
        
    def getArea(self):
        return self.base * self.height / 2
    
t1 = Triangle(45,7)
print('삼각형의 넓이 :', t1.getArea())

t2 = Triangle()
t2.setTriangle(5,12)
print('삼각형의 넓이 :', t2.getArea())
'''