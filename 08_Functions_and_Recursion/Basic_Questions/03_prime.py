'''def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
number_check = 7
if is_prime(number_check):
    print(f"{number_check} is a prime number")
else:
    print(f"{number_check} is not a prime number")'''


import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
number_check = 45
if is_prime(number_check): 
    print(f"{number_check} is a prime number")
else:
    print(f"{number_check} is not a prime number")

number_check = 20
if is_prime(number_check): 
    print(f"{number_check} is a prime number")
else:
    print(f"{number_check} is not a prime number")