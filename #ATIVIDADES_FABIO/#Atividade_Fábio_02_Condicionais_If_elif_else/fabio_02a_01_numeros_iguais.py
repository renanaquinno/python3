#entrada

numero_um = int(input("INFORME O PRIMEIRO NUMERO: "))
numero_dois = int(input("INFORME O SEGUNDO NUMERO: "))
numero_tres = int(input("INFORME O TERCEIRO NUMERO: "))
um = 0
dois = 0
tres = 0


#processamento

def numeros_iguais ():
    if numero_um == numero_dois:
        um = 1
    if numero_dois == numero_tres:
        tres = 1
    if numero_um == numero_tres:
        dois = 1
    total = um + dois + tres
    if total == 1:
        iguais = 1
    else:
        iguais = 0
    
    total = um + dois + tres + iguais
    print("EXISTEM {} NÚMEROS IGUAIS".format(total))

#saida

numeros_iguais ()
