marks = int(input("enter the marks: "))
if 0<=marks<=100:
    match marks //10:
        case 10|9:
            print("Grade A.")
        case 8|7:
            print("Grade B.")
        case 6|5:
            print("Grade C.")
        case _:
            print("Fail")
else:
    print("Invalid Marks.")