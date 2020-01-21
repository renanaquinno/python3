#entrada
numero_um = int(input("INFORME O PRIMEIRO NUMERO: "))
numero_dois = int(input("INFORME O SEGUNDO NUMERO: "))
numero_tres = int(input("INFORME O TERCEIRO NUMERO: "))


#processamento
def maior_numero ():
    if numero_um > numero_dois and numero_um > numero_tres:
        maior = numero_um
    if numero_dois > numero_tres and numero_dois > numero_um:
        maior = numero_dois
    if numero_tres > numero_dois and numero_tres > numero_um:
        maior = numero_tres

    print("O MAIOR NÚMERO É {}".format(maior))

    
#saida
maior_numero()
