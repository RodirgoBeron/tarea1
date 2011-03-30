def  primo(m):
	n=2
	k=2
	while k <=m/2:
		if m%k == 0:
			n = n+1
			break
		k=k+1
	return n == 2


def listaprimos(m):
	p = range(1,m+1)
	l = []
	for ele in p:
		if primo(ele):
			l = l + [ele]
	return l
