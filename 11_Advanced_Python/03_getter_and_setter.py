class Person:
    def __init__(self, _name, _age):
        self._name = _name 
        self._age = _age
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @name.setter
    def name (self, new_name):
        self._name = new_name
    
    @age.setter
    def age(self, new_age):
        self._age = new_age

person = Person("John Doe", 35)
print(person.name)
print(person.age)

person.name = "Jane Doe"
person.age = 30

print(person.name, person.age)