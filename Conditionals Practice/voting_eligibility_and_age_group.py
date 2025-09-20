age = int(input("Enter the age of a person: "))
if age <= 0:
    print("Invalid age")
elif age < 18:
    print("Not eligible to vote.")
else:
    print("Eligible to vote. ")
    if age <= 30:
        print("Youth Voter")
    elif age <= 60:
        print("Middle age Voter")
    else:
        print("Senior Citizen Voter")