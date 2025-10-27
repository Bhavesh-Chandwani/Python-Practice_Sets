class Animal:
    def __init__(self, name):
        self.name =  name
        
    @property
    def speak(self):
        return f"{self.name} says Woofs!"

dog = Animal("Buddy")
print(dog.speak)    