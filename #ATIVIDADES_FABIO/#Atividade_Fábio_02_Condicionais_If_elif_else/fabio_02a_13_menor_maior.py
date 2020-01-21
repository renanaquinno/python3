#entrada

numero_um = int(input("INFORME O PRIMEIRO NUMERO: "))
numero_dois = int(input("INFORME O SEGUNDO NUMERO: "))
numero_tres = int(input("INFORME O TERCEIRO NUMERO: "))
numero_quatro = int(input("INFORME O QUARTO NUMERO: "))
numero_cinco = int(input("INFORME O QUINTO NUMERO: "))


#processamento

def maior_numero ():
    if numero_um > numero_dois and numero_um > numero_tres and numero_um > numero_quatro and numero_um > numero_cinco:
        maior = numero_um
    elif numero_dois > numero_um and numero_dois > numero_tres and numero_dois > numero_quatro and numero_dois > numero_cinco:
        maior = numero_dois
    elif numero_tres > numero_dois and numero_tres > numero_um and numero_tres > numero_quatro and numero_tres > numero_cinco:
        maior = numero_tres            
    elif numero_quatro > numero_um and numero_quatro > numero_dois and numero_quatro > numero_tres and numero_quatro > numero_cinco:
         maior = numero_quatro
    else:
        maior = numero_cinco 
            
    if  numero_um < numero_dois and numero_um < numero_tres and numero_um < numero_quatro and numero_um < numero_cinco:
        menor = numero_um
    elif numero_dois < numero_um and numero_dois < numero_tres and numero_dois < numero_quatro and numero_dois < numero_cinco:
        menor = numero_dois
    elif numero_tres < numero_dois and numero_tres < numero_um and numero_tres < numero_quatro and numero_tres < numero_cinco:
        menor = numero_tres            
    elif numero_quatro < numero_um and numero_quatro < numero_dois and numero_quatro < numero_tres and numero_quatro < numero_cinco:
         menor = numero_quatro
    else:
        menor = numero_cinco
            
    print("O MAIOR NÚMERO É {} E O MENOR É {}".format(maior,menor))

    
#saida

maior_numero()
