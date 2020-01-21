#entrada

numero = int(input())


#processamento

def determina_quantidade (numero):
    contador = 0
    while contador != numero:
        numero_dois = int(input())
        numero_tres = int(input())
        contador = numero_dois + numero_tres
        if contador != numero:
            numero_dois = int(input())
            contador = numero_tres + numero_dois
            if contador != numero:
                numero_tres = int(input())
                contador = numero_tres + numero_dois
        

        
    print(contador)
        


#saida

determina_quantidade(numero)
