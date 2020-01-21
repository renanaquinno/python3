#entrada e processamento

def valores ():
	positivos = 0
	contador = 0
	while contador < 6:
		numeros = float(input())
		contador += 1
		if numeros > 0:
			positivos += 1
	print("{} valores positivos".format(positivos))		


#saida

valores()