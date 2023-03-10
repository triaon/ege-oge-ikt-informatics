with open('26.txt', 'r') as f:
    a = [list(map(int, i.split())) for i in f]

matrix = [[] for _ in range(a[0][0])]
print(matrix)
del a[0]

for i in a:
    if len(matrix[i[0]]) < i[1]:
        matrix[i[0]] += [0 for i in range(i[1] - len(matrix[i[0]]))]
    # matrix[i[0]][i[1]] = 1

for j in matrix:
    print(*j)
