#entrada

entrada = input()
dados = entrada.split()

#processamento
def multiplus (dados):
    a = int(dados[0])
    b = int(dados[1])
    if a > b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a
    if maior % menor == 0:
        saida ="Sao Multiplos"
    else:
        saida ="Nao sao Multiplos"
    
    print(saida)
    
multiplus(dados)