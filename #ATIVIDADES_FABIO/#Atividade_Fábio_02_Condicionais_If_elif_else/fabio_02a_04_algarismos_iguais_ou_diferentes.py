#entrada

numero = int(input("INFORME UM NÚMERO DE DOIS DÍGITOS: "))


#processamento

dezena = numero // 10
unidade = numero % 10

def algarismo_igual ():
    if dezena == unidade:
        print("O ALGARISMO DA DEZENA É IGUAL AO DA UNIDADE")
    elif dezena > unidade:
        print("O ALGARISMO DA DEZENA É MAIOR DO QUE DA UNIDADE")
    else:
        print("O ALGARISMO DA DEZENA É MENOR DO QUE DA UNIDADE")


#saida

algarismo_igual()

