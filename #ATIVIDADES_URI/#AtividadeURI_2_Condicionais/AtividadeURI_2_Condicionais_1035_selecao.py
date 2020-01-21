#entrada

valores = input()
dados = valores.split()


#processamento
    
def selecao (dados):
    a = int(dados[0])
    b = int(dados[1])
    c = int(dados[2])
    d = int(dados[3])
    if b > c and d > a and (c+d) > (a+b) and c > 0 and d > 0 and a % 2 == 0:
        print("Valores aceitos")
    else:
        print("Valores nao aceitos")

		
#saida

selecao(dados)