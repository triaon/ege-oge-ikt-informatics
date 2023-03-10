with open('28130_B.txt', 'r') as f:
    a = [int(_) for _ in f]

del (a[0])

larger50 = [[] for _ in range(80)]
smaller50 = [[] for _ in range(80)]

for i in a:
    if i > 50:
        larger50[i % 80].append(i)
    else:
        smaller50[i % 80].append(i)

result = 0

for i in range(1, 40):
    result += len(larger50[i]) * len(smaller50[abs(80 - i)]) + len(smaller50[i]) * len(larger50[abs(80 - i)])
    # print()
    # print(len(larger50[i]) * len(smaller50[abs(80 - i)]) + len(smaller50[i]) * len(larger50[abs(80 - i)]))

result += len(smaller50[40]) * len(larger50[40])
result += len(smaller50[0]) * len(larger50[0])

print(result)
