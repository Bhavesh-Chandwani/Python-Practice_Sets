class Vehicle:
    def __init__(self, name, type):
        self.name = name
        self.type = type

#Single Inheritence
class Car(Vehicle):
    def __init__(self, name, type, gear, speed):
        super().__init__(name, type)
        self.gear = gear 
        self.speed = speed
    def get_info(self):
        print(f"The name of the car is {self.name}. Its type is {self.type} and its gear{self.gear}. Its top speed is {self.speed}km/hr")

#Multilevel Inheritence
class ElectricCar(Car):
    def __init__(self, name, type, gear, speed, environmental, maintenance ):
        super().__init__(name, type, gear, speed)
        self.environmental = environmental
        self.maintenance = maintenance
    def get_details(self):
        print(f"The name of the car is {self.name}. The type is {self.type}. The gear is {self.gear}. The top speed is upto {self.speed} km/hr . It is environmental{self.environmental} and its maintenance cost is {self.maintenance}")

#Object Creation
car = Car("BMW", "Petroleum"," Manual", "Upto 400" )
car.get_info()

electric_car = ElectricCar("Tata EV", "Battery","Automatic","220", "Friendly", "Low-Cost")
electric_car.get_details()