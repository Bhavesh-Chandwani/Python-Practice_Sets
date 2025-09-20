'''num = int(input("Enter the number: "))
for i in range (1,num):
    if i % 2!= 0:
        if (i + 2 >= num):
            print(i)                          #Way 1
        else:
            print(i , end = ",")'''

'''num = int(input("Enter the number: "))
for i in range (1,num+1,2):                    # way 2 printing the last number
    if i % 2!= 0:
        if (i + 2 > num):
            print(i)
        else:
            print(i , end = ",")'''

num = int(input("Enter the number: "))
for i in range (1, num if num % 2 == 0 else num +1, 2):   # Printing the odd number when the input is even.
    print(i, end =", " if i + 2 <= num else "")