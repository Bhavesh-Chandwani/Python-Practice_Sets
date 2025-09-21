n = int(input("Enter the number of rows: "))

# Upper pyramid
for i in range(1, n+1):
    for j in range(1, n-i+1):
        print("  ", end="")
    for k in range(1, 2*i):
        print("* ", end="")
    print()

# Lower pyramid
for i in range(n-1, 0, -1):
    for j in range(1, n-i+1):
        print("  ", end="")
    for k in range(1, 2*i):
        print("* ", end="")
    print()