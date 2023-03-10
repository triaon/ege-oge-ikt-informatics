print(max([len(i) for i in list(open('24(1).txt', 'r').readline().split('E')) if i.count('A') >= 3]))
