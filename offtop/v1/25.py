for i in range(200_000_000, 400_000_001):
    if i % 12 == 0:
        k = i // 12
        for j in range(2, int(k ** 0.5) + 1):
            if k % j == 0 and (j % 2 == 1 or (k // j) % 2 == 1):
                print(i)
                break
