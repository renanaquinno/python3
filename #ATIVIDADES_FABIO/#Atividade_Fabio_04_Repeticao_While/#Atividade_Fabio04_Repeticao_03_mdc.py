def valores ():
	valor1 = int(input())
	valor2 = int(input())

	contador = valor1

	while contador > 0:
		if valor1 % contador == 0 and valor2 % contador == 0:
			print("MDC", contador)
			break
		contador -= 1

#saida

valores()