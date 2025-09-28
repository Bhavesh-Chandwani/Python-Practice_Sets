def sum_oF_first_n_no(n):
    if n == 0:
        return 0
    return n + sum_oF_first_n_no(n-1)
print(sum_oF_first_n_no(5))