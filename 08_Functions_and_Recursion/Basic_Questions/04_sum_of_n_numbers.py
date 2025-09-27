def sum_of_n_numbers(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
sum_first_n_numbers = 10
print(sum_of_n_numbers(sum_first_n_numbers))