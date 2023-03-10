with open('24(3).txt', 'r') as f:
    a = [i for i in f if i.count("G") < 25]

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
max_val = 0
for i in a:
    for j in alphabet:
        max_val = max(max_val, i.rfind(j)-i.find(j))

print(max_val)
