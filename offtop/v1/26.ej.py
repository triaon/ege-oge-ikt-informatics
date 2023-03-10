with open('26.txt', 'r') as f:
    db = [list(map(int, _.split())) for _ in f]
del (db[0])

start_time = 1634515200
end_time = start_time + 7 * 24 * 60 * 60
a = [0 for _ in range(start_time, end_time + 1)]


def increase(m, n):
    global a
    for j in range(m, n):
        a[j - start_time] += 1


for i in db:
    if (i[0] >= start_time) and (i[0] < end_time):
        if i[1] == 0 or i[1] >= end_time:
            increase(i[0], end_time + 1)
        elif i[1] < end_time:
            increase(i[0], i[1])
    elif i[0] < start_time:
        if i[1] == 0 or i[1] >= end_time:
            increase(start_time, end_time + 1)
        elif i[1] < end_time:
            increase(start_time, i[1])

print(max(a), a.count(max(a)))
