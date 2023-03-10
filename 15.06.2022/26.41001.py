start = 1634515200
end = start + 7 * 24 * 60 * 60

with open('26(1).txt', 'r') as f:
    all_vals = [[max(int(i.split()[0]), start), min(int(i.split()[1]), end)] for i in f if len(i.split()) > 1]

starts = []
ends = []
for i in range(len(all_vals)):
    if all_vals[i][1] == 0:
        ends.append(end)
    else:
        ends.append(all_vals[i][1])

    starts.append(all_vals[i][0])
c = 0
res = []
max_val = 0
timer = 0
max_time = 0
for i in range(start, end):
    c += starts.count(i)
    c -= ends.count(i)
    if c == max_val:
        timer += 1
    elif c > max_val:
        timer = 1
    max_time = max(max_time, timer)
    max_val = max(c, max_val)

print(max_val, max_time)
