num = int(input("Enter the number: "))
for i in range(1,num):
    if (i == num - 1):
        print (i)
    else:
        print(i, end = ", ")