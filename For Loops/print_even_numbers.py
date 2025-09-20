num = int(input("Enter the nmumber: "))
for i in range (2, num):
    if (i % 2 == 0 ):
        if (i == num-1) or i+2 >= num:
            print (i)
        else:
            print(i, end = ", ")
    