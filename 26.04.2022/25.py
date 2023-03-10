counter = 600001
result = []
while len(result) < 5:
    for i in range(7, counter, 10):
        if counter % i == 0:
            if i % 10 == 7 and i != 7:
                result.append((counter, i))
                break
    counter += 1

print(*result)
