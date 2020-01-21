#entrada

n = int(input())


#processamento

def resto_dois (n):
	contador = 0
	while contador < 10000:
		contador += 1
		if contador % n == 2:
			print(contador)
	
  	
#saida

resto_dois(n)
