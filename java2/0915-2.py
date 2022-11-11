class Cal:
    def __init__(self,x,y):
        self.x =x
        self.y = y
        self.calc2 = Cal2(x,y) #Cal2의 생성자가 매개변수 두개를 받기로 했기때문
    def add(self):
        return self.x+ self.y

a = Cal(10,10)
hasattr(a,'x') #x라는 객체(변수)가 있는가! 인데 문자열로 물어봐야함~
setattr(a,'x',20) # a의 x를 20으로 세팅

#파이썬엔 메소드 오버로딩이 없음
# 오버로딩   : 같은 이름이지만 매개변수 개수나 유형이 다르게 정해주는것
# 오버라이딩 : 부모에서 상속받은 메소드를 수정하는것. 이거 덮으면 부모늬 내용 싹 사라짐.
#안없애고 싶으면, super.어쩌고 라고 써주면 그대로 가져오게 됨


