#entrada

valores = input().split()



#processamento
def bhaskara (valores):
	r1 = 0
	r2 = 0
	a = float(valores[0])
	b = float(valores[1])
	c = float(valores[2])
	
	delta = (b**2)-(4*a*c)
	
	if a == 0:
		print("Impossivel calcular")
	elif delta > 0:
		sqdelta = delta ** (1/2)
		r1 = (-(b) + sqdelta) / (2 * a)
		r2 = (-(b) - sqdelta) / (2 * a)
		print("R1 = {:.5f}".format(r1))
		print("R2 = {:.5f}".format(r2))
	else:
		print("Impossivel calcular")
		
		
		
	
#saida

bhaskara(valores) 