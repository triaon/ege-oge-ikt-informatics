with open('24.txt', 'r') as f:
    a = f.readline()
line = ''
max_len = 0
for i in range(len(a)):
    if 'ad' not in line and 'da' not in line:
        line += a[i]
    else:
        max_len = max(max_len, len(line) - 1)
        line = a[i - 1] + a[i]

max_len = max(max_len, len(line) - 1)

print(max_len)
