class Parallelogram:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        
    def get_area(self):
        return self.length * self.width
    
class Square(Parallelogram):
    def __init__(self, width):
        super().__init__(width, length=width)
        
    def get_area(self):
        return self.width**2
    
para = Parallelogram(10, 5)
print(para.get_area())
sq = Square(90)
print(sq.get_area())

