result = []
i = 39 * 11

while len(result) < 5:
    d_count = []
    for k in range(1, int(i ** 0.5) + 1):
        if i % k == 0:
            if (k % 1000) // 10 == 42:
                d_count.append(k)
            if ((i // k) % 1000) // 10 == 42:
                d_count.append(i // k)
    if len(d_count) == 2:
        result.append([i]+sorted(d_count))

    # i += 1
    i += 11

print(*result)
