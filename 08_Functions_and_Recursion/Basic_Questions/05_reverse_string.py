def reverse_string(string):
    result = " "
    for ch in string:
        result = ch + result
    return result
string = "Bhavesh"
print(reverse_string(string))