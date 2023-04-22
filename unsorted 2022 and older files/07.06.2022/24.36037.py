with open('24(1).txt', 'r') as f:
    a = f.readline()

string = ''
max_length = 0

for i in a:
    string += i
    if 'XZZY' in string:
        max_length = max(max_length, len(string) - 1)
        string = 'ZZY'

print(max_length)
