#entrada

numero = float(input("DIGITE UM NUMERO FRACIONADO: "))

#processamento

fracionado = (numero % 1)

def arredonda ():
    if fracionado >= 0.5:
        aumento_fracao = 1 - fracionado
        aumento_fracao = aumento_fracao + numero
        print(f"O NÚMERO ARREDONDADO PARA CIMA É {aumento_fracao}")
    elif fracionado < 0.5:
        diminui_fracao = numero - fracionado
        print(f"O NÚMERO ARREDONDADO PARA BAIXO É {diminui_fracao}")
    else:
        print("VOCÊ NÃO DIGITOU UM NÚMERO FRACIONADO")

#saida 

arredonda()