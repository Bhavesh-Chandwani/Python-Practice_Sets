'''tuple = (10,20,30,40)
print(tuple.index(40))
'''
numbers = (10, 20, 30, 40)

try:
    pos = numbers.index(40)   # 50 is not in tuple
    print(f"Element found at index {pos}")
except ValueError:
    print("Element not found in tuple")