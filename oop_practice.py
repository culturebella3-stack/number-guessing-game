class Car:
 def __init__(self, brand, color ):
   self.brand = brand
   self.color = color
   self.speed = 0

 def drive(self):
    print(f"The {self.brand} is driving!")

 def honk(self):
    print(f"The {self.color} {self.brand} goes beep beep")

 def accelerate(self):
    self.speed += 10
    print(f"The {self.brand} is now going {self.speed}km/h!")

my_car = Car("Toyota", "red")
print(my_car.brand)  
my_car.drive()

my_car2 = Car("Honda", "blue")
my_car2.drive()
                  
my_car.honk()
my_car2.honk()                  

my_car.accelerate()
my_car.accelerate()
my_car.accelerate()