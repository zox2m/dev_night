class Cal:
    def __init__(self,x,y):
        self.x =x
        self.y = y
        self.calc2 = Cal2(x,y) #Cal2의 생성자가 매개변수 두개를 받기로 했기때문

    #정적메소드가 되면 인스턴스화 하지 않고 호출가능. 독립적으로 사용하기 때문에 다른 속성에
    # 클래스 멤버는 지역변수와 달리 객체 생성 전에 클래스만 불릴때 이미 생성되는데
    #그거랑 같은 개념인가?!

    #골뱅이 이름은 데코레이터!
    
    @staticmethod # add 메소드를 정적 메소드로 만드는 코드!
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

class Person:
    count =0

    def __init__(self):
        Person.count += 1
        # 인스턴스가 만들어질 때 count에 1을 더함

    def print_cout(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))  #format쓰는법! 
        #cls로 클래스 속성에 접근.
        #cls는 현재 틀래스를 뜩함


#self와 cls. 인스턴스는 self쓰고 클래스속성은 cls. 
    @classmethod
    
