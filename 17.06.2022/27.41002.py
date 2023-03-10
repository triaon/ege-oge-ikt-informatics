with open('27-B(1).txt', 'r') as f:
    allVals = list(map(int, f.readlines()))

del allVals[0]

d = [99999999 for i in range(30)]
d[0] = 0
sumVal = counter = result = 0
for i in range(len(allVals)):
    sumVal += allVals[i]
    if allVals[i] % 2 == 1 and allVals[i] > 0:
        counter += 1
    d[counter % 30] = min(d[counter % 30], sumVal)
    result = max(sumVal - d[counter % 30], result)

print(result)
