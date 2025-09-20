n = int(input("Enter the number: "))
i = n
while i>=1:
    if i > 1:
        print(i, end = ",")
    else:
        print(i)
    i-=1
print("Loop ends.")