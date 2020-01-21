#entrada

numero = float(input())


#processamento

def valor (numero):
    
    if numero >= 0 and numero <= 25:
        numero = "Intervalo [0,25]"
    elif numero > 25 and numero <= 50:
        numero = "Intervalo (25,50]"
    elif numero > 50 and numero <= 75:
        numero = "Intervalo (50,75]"
    elif numero > 75 and numero <= 100:
        numero = "Intervalo (75,100]"
    else:
        numero = "Fora de intervalo"    	
       
    print(numero)

	
#saida

valor (numero)