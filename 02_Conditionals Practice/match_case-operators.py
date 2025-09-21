num_1 = int(input("Enter the first number: "))
operator = input("Enter the operator (+,-,*,/,%,//,**): ")
num_2 = int(input("Enter the second number: "))

match operator:
    case "+":
        print(num_1+num_2)
    case "-":
        print(num_1-num_2)
    case "*":
        print(num_1*num_2)
    case "/":
        print(num_1/num_2)
    case "%":
        print(num_1%num_2)
    case "//":
        print(num_1//num_2)
    case "**":
        print(num_1**num_2)
    case _:
        print("Invalid Operator: ")