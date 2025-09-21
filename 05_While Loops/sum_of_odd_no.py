n = int(input("Enter the number: "))
i =  1
sum = 0
while i <=n:
    if i % 2 != 0:
        sum += i
    i += 1
print(f"The sum of odd number is {sum}")