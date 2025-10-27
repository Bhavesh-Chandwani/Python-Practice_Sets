num = [2,3,4,5,8,11,14,9]
filtered_num = filter(lambda x : x % 2 == 0, num)
print(list(filtered_num))