#processamento

def main():
	p1 = input().split( )
	p2 = input().split( )
	x1, y1 = p1
	x2, y2 = p2
	x = ((float(x2) - float(x1)))**2
	y = ((float(y2) - float(y1)))**2
	quadrado = (x + y) ** 2
	quadrado = quadrado ** (1/2)
	quadrado = quadrado ** 0.5
	print("{:.4f}".format(quadrado))


#saida
	
main ()