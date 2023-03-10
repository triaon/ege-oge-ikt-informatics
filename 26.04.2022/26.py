with open('26.txt', 'r') as f:
    a = [list(int(i.split()[0]), (i.split()[1])) for i in f]

m = a[0]
del a[0]
a.sort()
# for i in a:

