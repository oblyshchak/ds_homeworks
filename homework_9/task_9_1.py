class Car:
    def __init__(self, model, color, engine):
        self.color = color
        self.model = model
        self.engine = engine
        
    def forward(self):
        print(f"Car {self.model} drives forward")
    
    def back(self):
        print(f"Car {self.model} drives back")


class NewCar(Car):
    def __init__(self, model, color, engine):
        super().__init__(model, color, engine)
        
    def turn_left(self):
        print(f"Car {self.model} turns left")
        
    def turn_right(self):
        print(f"Car {self.model} turns right")

 
car1 = Car('hyundai accent', 'black', 1.6)
print(car1.forward())

car2 = NewCar('bmw i3', 'blue', 'electric')
print(car2.turn_left())
print(car2.forward())