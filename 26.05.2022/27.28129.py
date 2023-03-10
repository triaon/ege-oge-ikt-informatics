with open('28129_A.txt') as f:
    a = [int(_) for _ in f]

del (a[0])

div7 = [[-100000000000] for _ in range(160)]
divNot7 = [[-100000000000] for _ in range(160)]

for i in a:
    if i % 7 == 0:
        div7[i % 160].append(i)
    else:
        divNot7[i % 160].append(i)

res = list()
for i in range(160):
    div7[i].sort()
    divNot7[i].sort()

for i in range(160):
    for j in range(160):
        if i != j:
            res.append(div7[i][-1] + div7[j][-1])
            res.append(div7[i][-1] + divNot7[j][-1])
            res.append(div7[j][-1] + divNot7[i][-1])

print(max(res))
