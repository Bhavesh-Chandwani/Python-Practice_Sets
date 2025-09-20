s = input("Enter the string: ")
count_digit = 0
count_alpha = 0
count_space = 0
count_sc = 0
for ch in s:
    if ch.isdigit():
        count_digit += 1
    elif ch.isalpha():
        count_alpha += 1
    elif ch.isspace():
        count_space += 1
    else:
        count_sc += 1
print(f"Number of Alphabets are {count_alpha}\n Number of Digits are {count_digit}\n Number of Spaces are {count_space}\n Number of Special Charcters are {count_sc}")


# Counting uppercase and lower case character separately
s = input("Enter the string: ")
count_digit = 0
count_upper = 0
count_lower = 0
count_space = 0
count_sc = 0
for ch in s:
    if ch.isdigit():
        count_digit += 1
    elif ch.isupper():
        count_upper += 1
    elif ch.islower():
        count_lower += 1
    elif ch.isspace():
        count_space += 1
    else:
        count_sc += 1
print(f"Number of Upper Case Alphabets are {count_upper}\n Number of Lower Case Alphabets are {count_lower}\n Number of Digits are {count_digit}\n Number of Spaces are {count_space}\n Number of Special Charcters are {count_sc}")