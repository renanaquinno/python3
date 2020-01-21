#entrada

num_um = int(input("Informe o Primeiro Numero: "))
num_dois = int(input("Informe o Segundo Numero: "))


#processamento

def determina_mdc (num_um, num_dois):
    if num_um > num_dois:
        maior = num_um
        menor = num_dois
    else:
        maior = num_dois
        menor = num_um
    while menor > 0:
        if maior % menor != 0:
            menor = maior % menor
            maior = maior - menor        
        else:
            maior = maior - menor
            menor = 0
    print(maior)
                   

#saida

determina_mdc(num_um, num_dois)