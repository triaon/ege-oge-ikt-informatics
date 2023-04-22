print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if (((x <= y) == (z <= w)) or (x and w)) == 0:
                    print(x, y, z, w)
"""
3 2 1 4
x y z w
0 0 1 0
0 1 1 0
1 0 0 0 --
1 1 1 0
"""
