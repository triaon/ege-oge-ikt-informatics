div14 = []
div7 = []
div2 = []
another = []
with open('27-B_2.txt', 'r') as f:
	for i in f:
		if int(i)%14==0:
			div14.append(int(i))
		elif int(i)%7==0:
			div7.append(int(i))
		elif int(i)%2==0:
			div2.append(int(i))
		else:
			another.append(int(i))

div14.sort()

print(max( max(another)*div14[-1], div14[-1]*div14[-2], div14[-1]*max(div2), div14[-1]*max(div7), max(div7)*max(div2) ))
