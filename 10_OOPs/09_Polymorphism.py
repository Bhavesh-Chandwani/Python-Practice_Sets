class Animal:
    def speak(self):
        print (f"Genric Animal sound is")
class Dog(Animal):
    def speak(self):
        print (f"Dog Barks!")    
class Cat(Animal):
    def speak(self):
        print (f"Cat Meows!") 
class Cow(Animal):
    def speak(self):
        print (f"Cow Moos!")
for animal in [Dog(), Cat(), Cow()]:
    animal.speak()      #Same Method Different Behaviours
