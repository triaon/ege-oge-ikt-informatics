print(max([len(i) for i in open('24(2).txt', 'r').readline().replace('ad', 'a*d').replace('da', 'd*a').split('*')]))
