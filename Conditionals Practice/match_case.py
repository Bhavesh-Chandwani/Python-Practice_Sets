a = int(input('Enter the number between 1-10: '))
if 1<=a<=10:
    match a:
        case 1:
            print("You won the camera.")
        case 3:
            print("You won an iphone.")
        case 5:
            print("You won $5.")
        case _:
            print("Better Luck Next Time.")
else:
    print("Invalid Number! Please Enter Number between 1-10")