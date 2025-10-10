class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def get_info(self):
        print(f"The brand of the car is {self.brand} and the model is {self.model} and year of manufacturing is {self.year}")
car_1 = Car("BMW", "Z4", 2020)
car_1.get_info()

car_2 = Car("Ford", "Mustang", 1969)
car_2.get_info()