n = int(input("Enter the number: "))
count = 0
while n > 0:
    n = n // 10
    count+=1
print(f"Total Number of Digits is {count}")