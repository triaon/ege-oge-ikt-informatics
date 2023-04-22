with open('24.txt', 'r') as f:
    a = f.readline()

string = ''
i = 0
max_length = 0
while i < len(a) - 1:
    if len(string) <= 1:
        string += a[i]
    print(string)
    if a[i] != string[-1] and a[i] == a[i + 1]:
        if len(string) > 2:
            max_length = max(len(string), max_length)
        i += 1
    elif a[i] == string[-1] and a[i] == a[i + 1]:
        string = 2 * a[i]
        i += 1

    i += 1

print(max_length)
