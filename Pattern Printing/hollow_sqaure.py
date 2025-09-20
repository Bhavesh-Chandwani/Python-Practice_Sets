'''
*****
*   *
*   *
*   *
*****
'''

n = int(input("Enter the number of rows: "))
for i in range (1, n+1):
    if i == 1 or i == n:
        for j in range (1, n+1):
            print("* ", end = " ")
    else:
        for k in range(1, n+1):
            if k == 1 or k == n:
                print("* ", end = " ")
            else:
                print("  ", end = " ")
    print()