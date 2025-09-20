s = input("Enter the string: ")
shift = 2
result = ""
for ch in s:
    if ch.isalpha():
        if ch.islower():
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        
        elif ch.isupper():
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    else:
        result += ch
print(f"Encryption is : {result}")