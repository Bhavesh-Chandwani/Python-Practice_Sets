num = int(input("Enter the number: "))
for i in range(1, num):
    if i%2==0:
        if i + 2 >= num:
            print(i)
        else:
            print(i, end = ", ")