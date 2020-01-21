#entrada e processamento

def valores ():
	par = 0
	contador = 0
	while contador < 5:
		numeros = int(input())
		contador += 1
		if numeros % 2 == 0:
			par += 1
	print("{} valores pares".format(par))		


#saida

valores()