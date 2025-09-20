num = int(input("Enter the number: "))
if(num % 3 == 0 and num % 5 == 0):
    print("Divisible by both 3 and 5")
elif(num % 3 ==0):
    print("Divisible only by 3")
elif(num % 5 ==0):
    print("Divisible only by 5")
else: 
    print("Not divisible by 3 or 5")
