n = int(input("Enter the number: "))
i = 1
while i<=n:
    if i % 2 != 0:
        if i + 2 > n:
            print(i)
        else:
            print(i, end = ",")
    i+=1