#20
def f(a, b, pv, c):
	if c < 4:
		return False
	elif a + b >= 47:
		return not pv
	elif pv:
		return f(a+1, b+2, pv, c+1) or f(a+2, b+1, pv, c+1) or f(a*2, b, pv, c+1) or f(a, b*2, pv, c+1)
	else:
		return f(a+1, b+2, pv, c+1) and f(a+2, b+1, pv, c+1) and f(a*2, b, pv, c+1) and f(a, b*2, pv, c+1)


for s in range(1, 36):
	if f(10, s, True, 1):
		print(s)
