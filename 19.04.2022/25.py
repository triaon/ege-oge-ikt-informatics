def m(n):
    v = list()
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            v.append(i)
        if len(v) == 5:
            break
    if len(v) < 5:
        return 0
    else:
        mul = lambda arr: arr[0] * mul(arr[1:]) if arr else 1
        return mul(v)


vals = list()
counter = 500000001
while len(vals) < 5:
    if m(counter) != 0:
        vals.append(m(counter))
    counter += 1
print(*vals)
