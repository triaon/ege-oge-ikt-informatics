def f(n, s):
    if s == 4 and n >= 35:
        return True
    elif n >= 35:
        return False
    elif s > 4:
        return False
    if s % 2 == 1:
        return f(n * 2, s + 1) or f(n + 3, s + 1) or f(n + 1, s + 1)
    else:
        return f(n * 2, s + 1) and f(n + 3, s + 1) and f(n + 1, s + 1)


for i in range(35):
    if f(i, 1):
        print(i)
