class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def get_info(self):
        print(f"The name of the student is {self.name} and the roll no is {self.roll_no} and the marks scored {self.marks}")
student = Student("John Doe", 1 , 95)
student.get_info()