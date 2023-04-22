with open('24.txt', 'r') as f:
    a = f.readline()

substring = ''
c = ''  # подподстрока, состоящая из AAA или BB и тп
results = []  # тут все подстроки
max_len = 0
for i in range(1, len(a)):
    if c == '':
        c += a[i]
    elif c[-1] == a[i]:
        c += a[i]
    else:
        if len(c) == 2:
            substring += c
            c = a[i]
        elif len(c) > 2:
            substring = substring[2:]
            print(c, substring)
            # вывод подподстроки с повторяющимися элементами, на котором заканчивается подстрока и подстрока без нее
            c = a[i - 1] * 2
            max_len = max(max_len, len(substring) + 2)
            results.append(substring + c)
            substring = c
        # else:
        #     if substring != '':
        #         print(c, substring)
        #         c = ''
        #         max_len = max(max_len, len(substring))
        #         results.append(substring)
        #         substring = ''
        # что-то лишнее, ответ слишком маленький, подстроки ломаются

print(results)  # все подстроки

print(max_len)  # максимальная длина

print(results[[len(i) for i in results].index(80)])  # элемент, имеющий максимальную длину (80)
