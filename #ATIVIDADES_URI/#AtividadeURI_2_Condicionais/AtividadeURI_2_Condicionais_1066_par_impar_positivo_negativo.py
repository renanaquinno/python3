#entrada e processamento

def valores ():
	contador = 0
	par = 0
	impares = 0
	positivos = 0
	negativos = 0
	while contador < 5:
		numeros = int(input())
		contador += 1
		if numeros % 2 == 0:
			par += 1
		elif numeros % 2 != 0:
			impares += 1
		if numeros > 0:
			positivos += 1
		elif numeros < 0:
			negativos += 1

	print("{} valor(es) par(es)".format(par))
	print("{} valor(es) impar(es)".format(impares))
	print("{} valor(es) positivo(s)".format(positivos))
	print("{} valor(es) negativo(s)".format(negativos))



#saida

valores()