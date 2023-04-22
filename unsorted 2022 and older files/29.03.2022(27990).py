div62 = 0
div31 = 0
div2 = 0
another = 0
with open('231-B_2.txt', 'r') as f:
	for i in f:
		if int(i)%62==0:
			div62 += 1
		elif int(i)%31==0:
			div31 += 1
		elif int(i)%2==0:
			div2 += 1
		else:
			another += 1

print(div62*(div2+div31+another) + div2*div31 + sum(range(div62)))
