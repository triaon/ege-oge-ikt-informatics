a = []
p = 1
while p < 35000000000:
    a.append(p)
    p *= 7
print(a)  # вывожу степени 7 для себя


def f(n):
    if n == 0:
        return 0
    if n % 7 == 0:
        return f(n // 7)
    return f(n - 1) + 1


res = []
for i in range(13841287201 - 10, 13841287202):
    res.append(f(i))
for i in range(35000000000 - 10, 35000000001):
    res.append(f(i))
for i in range(int('2266666666666', 7) - 10, int('2266666666666', 7) + 10):  # int для перевода из 7-ной сс
    res.append(f(i))
print(res)  # результаты от f
print(max(res))  # наибольшее из результатов
