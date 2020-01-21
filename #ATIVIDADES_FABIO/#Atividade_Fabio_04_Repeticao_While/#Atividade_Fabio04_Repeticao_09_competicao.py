#entrada e processamento


def competicao ():
	num_prova = int(input("N. prova: "))
	qtd_nadadores = int(input("Nadadores: "))
	pontos_a = 0
	pontos_b = 0

	while  not (num_prova == 0 and qtd_nadadores == 0):

		while  qtd_nadadores > 0:
			#pedir os dados
			nome = input("Nome: ")
			classificacao = int(input("Classificacao: "))
			tempo = int(input("Tempo: "))
			clube = input("Clube: ")
			while  clube != "a" and clube != "b":
				clube = input("Clube: ")	
			
			if clube == "a":
				pontos_a += calcular_pontos(classificacao)
			else:
				pontos_b += calcular_pontos(classificacao)		
			qtd_nadadores -= 1


		num_prova = int(input("N. prova: "))
		qtd_nadadores = int(input("Nadadores: "))


	print("Clube A",pontos_a)
	print("Clube B",pontos_b)


	print("*****RESULTADO******")
	if pontos_a > pontos_b:
		print("Clube A venceu!")
	elif pontos_b < pontos_a:
		print("Clube B venceu!")
	else:
		print("Empate")

		


def calcular_pontos ():
	if classificacao == 1: return 9 
	if classificacao == 2: return 6 
	if classificacao == 3: return 4 
	if classificacao == 4: return 3

	return 0


#saida

competicao()