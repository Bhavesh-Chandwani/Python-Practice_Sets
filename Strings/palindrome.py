s = input("Enter the string: ")
s_clean = s.lower().replace(" ", "")
if s_clean == s_clean[::-1]:
    print(f"Given {s} string is Palindrome.")
else:
    print(f"Givem {s} string is not a Palindrome")