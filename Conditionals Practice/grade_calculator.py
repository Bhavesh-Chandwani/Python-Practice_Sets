ITM = int(input("Enter the ITM Marks: "))
DA = int(input("Enter the DA Marks: "))
PROJECT = int(input("Enter the PROJECT Marks: "))
OST = int(input("Enter the OST Marks: "))
NS = int(input("Enter the NS Marks: "))
total_marks = ITM+DA+PROJECT+OST+NS
percentage = (total_marks/500)*100
print (f"The Percentage of the Student is {percentage}%", end = "\n\n")
print("Lets Distribute the Grade to the Student according to their percentage they scored :-", end = "\n\n")

if(percentage >= 90):
    print ("Grade A+! Excellent")
elif(percentage >=80 and percentage < 90):
    print("Grade A! Very Good")
elif(percentage >=70 and percentage < 80):
    print("Grade B+! Good")
elif(percentage >=60 and percentage < 70):
    print("Grade B! Well Done")
elif(percentage >=50 and percentage < 60):
    print("Grade C! Need to do Better.")
elif(percentage >=40 and percentage < 50):
    print("Grade D! Improve yourself")
else:
    print("You're fail")