b = []
d = 0
for i in open('24(4).txt', 'r'):
    b.append([i.count('N'), d, i])
    d += 1
a = min(b)[2]
print(max([[a.count(j), j] for j in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[::-1]]))
