class Cal:
    def __init__(self,x,y):
        self.x =x
        self.y = y
        self.calc2 = Cal2(x,y) #Cal2의 생성자가 매개변수 두개를 받기로 했기때문
    def add(self):
        return self.x+ self.y
    def multiply(self):
        return self.calc2.muliply()

class Cal2:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    def multiply(self):
        return self.x*self.y
