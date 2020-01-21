#entrada

numero_um = int(input("INFORME O PRIMEIRO NUMERO: "))
numero_dois = int(input("INFORME O SEGUNDO NUMERO: "))
numero_tres = int(input("INFORME O TERCEIRO NUMERO: "))


#processamento

def numeros_crescentes ():
    if numero_um > numero_dois and numero_um > numero_tres:
        maior = numero_um
    elif numero_dois > numero_tres and numero_dois > numero_um:
        maior = numero_dois
    else:
        maior = numero_tres

    if numero_um > numero_dois and numero_um < numero_tres:
        meio = numero_um
    elif numero_dois > numero_tres and numero_dois < numero_um:
        meio = numero_dois
    else:
        meio = numero_tres

    if numero_um < numero_dois and numero_um < numero_tres:
        menor = numero_um
    elif numero_dois < numero_tres and numero_dois < numero_um:
        menor = numero_dois
    else:
        menor = numero_tres
    
    print(menor, meio, maior)
    
    
#saida

numeros_crescentes()


