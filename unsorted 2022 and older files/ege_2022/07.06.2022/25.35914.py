res = list()

for i in range(45_000_000, 50_000_001):
    a = i
    while a % 2 == 0:
        a //= 2
    if a ** (1 / 4) == int(a ** (1 / 4)):
        res.append([i, int(a ** (1 / 4))])

print(*res)
