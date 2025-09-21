num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))

if(num_1 == num_2 == num_3):
    print(f"All numbers are equal")

elif(num_1 >= num_2 and num_1 >= num_3):
    if(num_1 == num_2):
        print(f"{num_1} is largest and appears at position 1 and 2 respectively.")
        '''
        In the above if block we took {num_1} just to represent the number.
        We can alse take {num_2}, In the rest code we will use the same format.
        '''
    elif(num_1 == num_3):
        print(f"{num_1} is largest and appears at position 1 and 3 respectively.")
    else:
        print(f"{num_1} is largest and appears at position 1.")

elif(num_2 >= num_3):
    if(num_2 == num_3):
        print(f"{num_2} is largest and appears at position 2 and 3 respectively.")
    else:
        print(f"{num_2} is largest and appears at position 2.")

else:
    print(f"{num_3} is largest and appears at position 3.")