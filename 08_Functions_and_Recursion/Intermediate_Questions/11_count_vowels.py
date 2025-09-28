def count_vowels(s):
    if len(s) == 0:
        return 0
    if s[0].lower() in "aeiou":
        n = 1
    else:
        n = 0
    return n + count_vowels(s[1:])
print(count_vowels("Bhavesh"))