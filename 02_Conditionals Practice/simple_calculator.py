first_number = int(input("Enter the 1st number: "))
operator = input("Enter the operator(+,-,*,/,%,//,**): ")
second_number = int(input("Enter the 2nd number: "))
if (operator == "+"):
    print (first_number + second_number)
elif (operator == "-"):
    print (first_number - second_number)
elif (operator == "*"):
    print (first_number * second_number)
elif (operator == "/"):
    print (first_number / second_number)
elif (operator == "%"):
    print (first_number % second_number)
elif (operator == "//"):
    print (first_number // second_number)
elif (operator == "**"):
    print (first_number ** second_number)
else:
    print("Invalid Operator")

