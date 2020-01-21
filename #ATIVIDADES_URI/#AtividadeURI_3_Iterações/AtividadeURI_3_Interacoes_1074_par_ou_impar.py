#entrada

n = int(input())


#processamento

def par_impar (n):
	contador = 0
	while contador < n:
		contador += 1
		valor = int(input())
		if valor == 0:
			print("NULL")
		elif valor % 2 == 0:
			if valor < 0:
				print("EVEN NEGATIVE")
			else:
				print("EVEN POSITIVE")
		else:
			if valor < 0:
				print("ODD NEGATIVE")
			else:
				print("ODD POSITIVE")
  
	
#saida

par_impar(n)
