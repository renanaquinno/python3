#entrada

numero_um = int(input("INFORME O PRIMEIRO NUMERO: "))
numero_dois = int(input("INFORME O SEGUNDO NUMERO: "))
numero_tres = int(input("INFORME O TERCEIRO NUMERO: "))
numero_quatro = int(input("INFORME O QUARTO NUMERO: "))
numero_cinco = int(input("INFORME O QUINTO NUMERO: "))

#processamento

media = (numero_um + numero_dois + numero_tres + numero_quatro + numero_cinco) / 5 

def maior_media ():
    if numero_um > media:
        print(numero_um)
    if numero_dois > media:
        print(numero_dois)        
    if numero_tres > media:
        print(numero_tres)
    if numero_quatro > media:
        print(numero_quatro)
    if numero_cinco > media:
        print(numero_cinco)


#saida

maior_media()