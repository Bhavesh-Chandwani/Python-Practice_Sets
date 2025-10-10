class Flyable:
    def fly(self):
        return f"Fly"
class Swimmbale:
    def swim(self):
        return f"Swim"
#Multiple Inheritence
class Duck(Flyable, Swimmbale):
    def get_actions(self):
        print(f"Ducks can Fly and Swim")
duck = Duck()
print(duck.fly())
print(duck.swim())
duck.get_actions()