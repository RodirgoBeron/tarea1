def fibo(m):
	if m == 0:
		return 0
	elif m == 1:
		return 1
	else: return fibo(m-1) + fibo(m-2)

m = raw_input("introdusca n = ")
m = int(m)
print fibo(m)
m = raw_input()
