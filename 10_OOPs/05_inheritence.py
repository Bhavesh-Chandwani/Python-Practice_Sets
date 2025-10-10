#Parent Class or Super Class
class Person:
    def __init__(self, name):
        self.name = name

#Single Inheritence
class Teacher(Person):   #Child Class or Sub class
    def __init__(self, name, subject, salary):
        super().__init__(name)
        self.subject = subject   #Instance Attribute
        self.salary = salary     #Instance Attribute
    def get_info(self):
        return f"The name of the person is {self.name}.Teaches {self.subject} and salary is {self.salary} Rs"
    
# Object Creation
teacher = Teacher("John Doe","Python Programming", 50000)
print(teacher.name)
print(teacher.subject)
print(teacher.get_info())