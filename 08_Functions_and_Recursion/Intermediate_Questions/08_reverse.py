def func(n):
    if n == 0:
        return
    print(n, end = " ")
    func(n-1)
func(5)
