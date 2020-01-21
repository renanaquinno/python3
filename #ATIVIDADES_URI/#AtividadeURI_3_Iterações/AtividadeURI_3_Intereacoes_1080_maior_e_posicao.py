#entrada


# processamento

def maior_e_posicao ():
    contador = 0
    maior = 0
    valor = 0
    posicao = 0
    while contador < 100:
        valor = int(input())
        contador +=1
        if  maior < valor:
            maior = valor
            posicao = contador

    print(maior)        
    print(posicao)        


#saida

maior_e_posicao()