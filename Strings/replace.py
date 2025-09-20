'''s = input("Enter the String: ")
print(s.replace(" ", "-"))'''

'''# Replacement using for loop.
s = input("Enter the String : ").lower()
result = ""
for ch in s:
    if ch in " ":
        result += "-"
    else:
        result += ch
print(result)'''

'''# Replacing Vowels
s = input("Enter the String : ").lower()
result = ""
for ch in s:
    if ch in "aeiou":
        result += "*"
    else:
        result += ch
print(result)'''

 #Replacing Vowels with distinct special characters
s = input("Enter the String : ").lower()
result = ""
for ch in s:
    if ch in "aeiou":
        if ch in "a":
            result += "@"
        elif ch in "e":
            result += "#"
        elif ch in "i":
            result += "$"
        elif ch in "o":
            result += "%"
        elif ch in "u":
            result += "&"
    else:
        result+=ch
print(result)

