#entrada

numero_um = int(input("INFORME O PRIMEIRO NUMERO: "))
numero_dois = int(input("INFORME O SEGUNDO NUMERO: "))


#processamento

def maior_e_menor ():
    if numero_um == numero_dois:
        print("OS NÚMERO SÃO IGUAIS")
    elif numero_um > numero_dois :
        print(f"O NUMERO {numero_um} É O MAIOR")
    else:
        print(f"O NUMERO {numero_dois} É O MAIOR")


#saida

maior_e_menor()