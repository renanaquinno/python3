#entrada

valores = input().split()



#processamento
def triagulo (valores):
	valor_um = float(valores[0])
	valor_dois = float(valores[1])
	valor_tres = float(valores[2])
	a = 0
	b = 0
	c = 0
	
	if valor_um == valor_dois == valor_tres:
		a = valor_um
		b = valor_dois
		c = valor_tres
	
	elif valor_um > valor_dois > valor_tres:
		a = valor_um
		b = valor_dois
		c = valor_tres
		
	elif valor_um > valor_tres > valor_dois:
		a = valor_um
		b = valor_tres
		c = valor_dois
	
	elif valor_um == valor_dois > valor_tres:
		a = valor_um
		b = valor_dois
		c = valor_tres
		
	elif valor_um == valor_tres > valor_dois:
		a = valor_um
		b = valor_tres
		c = valor_dois
	
	elif valor_um == valor_dois < valor_tres:
		a = valor_tres
		b = valor_dois
		c = valor_um
	
	elif valor_um == valor_tres < valor_dois:
		a = valor_dois
		b = valor_tres
		c = valor_um
	
	elif valor_dois > valor_tres > valor_um:
		a = valor_dois
		b = valor_tres
		c = valor_um
	
	elif valor_dois == valor_tres > valor_um:
		a = valor_dois
		b = valor_tres
		c = valor_um
	
	elif valor_dois == valor_um > valor_tres:
		a = valor_dois
		b = valor_um
		c = valor_tres
	
	elif valor_dois > valor_um > valor_tres:
		a = valor_dois
		b = valor_um
		c = valor_tres
	
	elif valor_dois == valor_tres < valor_um:
		a = valor_um
		b = valor_tres
		c = valor_dois
	
	elif valor_dois == valor_um < valor_tres:
		a = valor_tres
		b = valor_um
		c = valor_dois
	
	elif valor_tres > valor_um > valor_dois:
		a = valor_tres
		b = valor_um
		c = valor_dois
	
	elif valor_tres > valor_dois > valor_um:
		a = valor_tres
		b = valor_dois
		c = valor_um
	
	elif valor_tres == valor_um > valor_dois:
		a = valor_tres
		b = valor_um
		c = valor_dois
	
	elif valor_tres == valor_dois > valor_um:
		a = valor_tres
		b = valor_dois
		c = valor_um
		
	elif valor_tres == valor_um < valor_dois:
		a = valor_dois
		b = valor_um
		c = valor_tres
	
	elif valor_tres == valor_dois < valor_um:
		a = valor_um
		b = valor_dois
		c = valor_tres
	
	if a >= (b + c):
		print("NAO FORMA TRIANGULO")
	else:	
		if a ** 2 == (b ** 2) + (c ** 2):
			print("TRIANGULO RETANGULO")
		if a ** 2 > (b ** 2) + (c ** 2):
			print("TRIANGULO OBTUSANGULO")
		if a ** 2 < (b ** 2) + (c ** 2):
			print("TRIANGULO ACUTANGULO")
		if a == b == c:
			print("TRIANGULO EQUILATERO")
		if a == b != c or a == c != b or b == c != a:
			print("TRIANGULO ISOSCELES")
		

#saida

triagulo(valores)
 
