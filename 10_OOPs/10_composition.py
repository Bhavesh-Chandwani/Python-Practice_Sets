class Battery:
    def __init__(self, capacity):
        self.capacity = capacity
    
    def get_capacity(self):
        return f"Battery Capacity is {self.capacity} mAh"

class Laptop:
    def __init__(self, brand, battery_capacity):
        self.brand = brand
        self.battery = Battery(battery_capacity)
    
    def get_details(self):
        return f" Brand : {self.brand}. {self.battery.get_capacity()}"

laptop = Laptop("Dell", 6500)
print(laptop.get_details())