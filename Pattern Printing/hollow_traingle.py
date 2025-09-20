'''n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    if i == 1 or i == 2 or i ==  n:
        for j in range (1, i+1):
            print("*", end = " ")
    else:
        for k in range (1, i + 1):
            if k == 1 or k == i:
                print("*", end = " ")
            else:
                print (" ", end = " ")
    print()'''

n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        if j == 1 or j == i or i == n:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()