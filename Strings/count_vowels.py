'''s = input("Enter the string: ")
count  = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count +=1
print(f"The number of vowels present in string is {count}")
    
'''

s = input("Enter the string: ").lower()
count = 0
for ch in s:
    if ch in "aeiou":
        count += 1
print(f"The number of vowels present in a string is {count}")
