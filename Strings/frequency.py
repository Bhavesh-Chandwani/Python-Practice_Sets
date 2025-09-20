'''s = input("Enter the string: ")
max_frequency = 0
most_frequent_character = []

for ch in set(s): # For unique elements
    freq = s.count(ch)
    if freq > max_frequency:
        max_frequency = freq
        most_frequent_character = [ch] #reset list with new max character.
    elif freq == max_frequency:
        most_frequent_character.append(ch)
print(f"Most frequent character {s}")
for ch in most_frequent_character:
    print(f"{ch} appears {max_frequency} times")'''

s = input("Enter the string: ")
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break