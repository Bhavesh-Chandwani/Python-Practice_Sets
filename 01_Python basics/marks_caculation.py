OST = int(input("Enter the marks: "))
NS = int(input("Enter the marks: "))
DA = int(input("Enter the marks: "))
CC = int(input("Enter the marks: "))
SPM = int(input("Enter the marks: "))

Total_Marks = OST+NS+DA+CC+SPM
print(f"The total marks of the Student is {Total_Marks}")
Average = Total_Marks/5
print(f"The average marks of the Student is {Average}")
Percentage = (Total_Marks/500)*100
print(f"The total Percentage of the Student is {Percentage:.2f}%") #.2f to include double decimal numbers