with open('28131_A.txt') as f:
    a = [int(_) for _ in f]

del a[0]
vals = [[] for _ in range(120)]
for i in range(len(a)):
    vals[a[i] % 120].append([a[i], i])

for i in range(120):
    vals[i].sort()

result = list()
for i in range(120):
    vals[i].sort()

for i in range(0, 61):
    for j in vals[i]:
        for k in vals[(120 - i) % 120]:
            if (j[1] < k[1] and j[0] > k[0]) or (j[1] > k[1] and j[0] < k[0]):
                result.append((j[0] + k[0], j[0], k[0]))

print(max(result))
