with open('27-B.txt', 'r') as f:
    a = [int(_) for _ in f]

del a[0]
results = 0

for i in range(len(a)):
    counter = 0
    div47, div131, div277 = (a[i] % 47 == 0), (a[i] % 131 == 0), (a[i] % 277 == 0)
    if i % 1705489 != 0:
        counter += 1
        for j in range(i + 1, len(a)):
            div47, div131, div277 = max(div47, (a[j] % 47 == 0)), max(div131, (a[j] % 131 == 0)), max(div277, (a[j] % 277 == 0))
            if div47 and div131 and div277:
                break
            else:
                counter += 1
        results += counter

print(results)

# 219690 a
# 609527278 b
