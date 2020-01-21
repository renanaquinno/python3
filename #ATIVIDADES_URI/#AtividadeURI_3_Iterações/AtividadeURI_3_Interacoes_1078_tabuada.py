#entrada

n = int(input())


#processamento

def tabuada (n):
	contador = 0
	while contador < 10:
		contador += 1
		multiplicao = n * contador
		print("{} x {} = {}".format(contador,n, multiplicao))
  	
	
#saida

tabuada(n)
