class Animal:
    def speak(self):
        return f"Genric Animal sound is"
class Dog(Animal):
    def speak(self):
        return f"Dog Barks!"    #Overridng the method of parent Class
class Cat(Animal):
    def speak(self):
        return f"Cat Meows!"    #Overridng the method of parent Class
dog = Dog()
print(dog.speak())

cat = Cat()
print(cat.speak())