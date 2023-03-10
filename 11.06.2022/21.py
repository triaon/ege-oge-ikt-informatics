def f(n, s):
    if s == 3 and n >= 35:
        return True
    if s == 5:
        if n >= 35:
            return True
        else:
            return False
    else:
        if n >= 35:
            return False
    if s % 2 == 1:
        return f(n * 2, s + 1) or f(n + 3, s + 1) or f(n + 1, s + 1)
    else:
        return f(n * 2, s + 1) and f(n + 3, s + 1) and f(n + 1, s + 1)


for i in range(35):
    if f(i, 1):
        print(i)

# def f(n, k):
#     if (k == 3) and (n >= 42):
#         return True
#     if (k == 5):
#
#     else:
#         if n >= 42:
#             return False
#     if k % 2 == 0:
#         return f(n+1, k+1) or f(n+5, k+1) or f(n*3, k+1)
#     else:
#         return f(n+1, k+1) and f(n+5, k+1) and f(n*3, k+1)
#
#
# for i in range(13):
#     if f(i, 1):
#         print(i)
