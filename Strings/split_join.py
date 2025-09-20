'''s = input("Enter the string: ")
str_splitting = s.split(" ")
print(f"The List of string after Split is {str_splitting}")
str_joining = ",".join(str_splitting)
print(f"The List after using Join is {str_joining}")
'''

#Joining the strings using distinct separators.
s = input("Enter the string: ")
words = s.split()
print(words)
joining_words = ";".join(words)
print(f"Joining word with semicolon: {joining_words}")
new_line_join = "\n".join(words)
print(f"Joining new line \n {new_line_join}")



