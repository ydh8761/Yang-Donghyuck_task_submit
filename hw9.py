class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

class Rectangle:
    def __init__(self,x1,y1,x2,y2):
        self.lt = Point(x1, y1)
        self.rb = Point(x2, y2)
    
    def show(self):
        print(f'좌측 상단 꼭지점이 ({self.lt.x},{self.lt.y})이고 우측 하단 꼭지점이 ({self.rb.x},{self.rb.y})인 사각형입니다.')
    def getWidth(self):
        return abs(self.lt.x - self.rb.x)
    def getHeight(self):
        return abs(self.lt.y - self.rb.y)
    def getArea(self):
        return self.getWidth() * self.getHeight()
    def getPerimeter(self):
        return 2 * (self.getWidth() + self.getHeight())
    
r1=Rectangle(5,5,20,10)
a=r1.getArea()
p=r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')