s1 = input("Enter the string 1: ").lower().replace(" " , "")
s2 = input("Enter the string 2: ").lower().replace(" " , "")
if sorted(s1) == sorted(s2):
    print(f"{s1} and {s2} are anagrams of each other.")
else:
    print(f"{s1} and {s2} are not anagrams of each other.")