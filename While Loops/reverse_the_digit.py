n = int(input("Enter the number: "))
original = n
reverse = 0
while n > 0:
    digits = n % 10 # Last Digit
    reverse = reverse * 10 + digits
    n = n //10
print(f"The reverse of {original} is {reverse}")