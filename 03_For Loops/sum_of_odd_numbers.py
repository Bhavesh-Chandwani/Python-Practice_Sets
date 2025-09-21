'''num = int(input("Enter the number: "))
sum = 0
for i in range (1, num if num % 2 == 0 else num +1, 2):
    sum += i   # Printing the odd number when the input is even.
    print(i, end =" + " if i + 2 <= num else " = ")
print(sum)'''

#Way 2 using lists.

num = int(input("Enter the number: "))
sum = 0
terms = []
for i in range (1, num+1):
    if i % 2 != 0:
        sum+=i
        terms.append(str(i))
print("+".join(terms), "=", sum)