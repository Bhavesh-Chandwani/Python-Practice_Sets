from functools import reduce
num = [1,2,3,4,5,6,7,8,9,10]
def add(a,b):
    return a + b
new_num = reduce(add, num)
print(new_num)