# Pyramid Pattern

n = int(input("Enter the number of rows: "))

for i in range(1, n+1):              # Outer loop for rows (1 to n)

    # Print spaces
    for j in range(1, n - i + 1):    # Spaces = n - i
        print("- ", end="")

    # Print stars
    for k in range(1, 2*i):          # Stars = 2*i - 1
        print("* ", end="")

    print()   # Move to next line after each row
