def f(m, n):
    if m > n:
        return 0
    elif m == n:
        return 1
    else:
        return f(m + 1, n) + f(m + 2, n) + f(m * 2, n)


print(f(3, 10) * f(10, 12))
