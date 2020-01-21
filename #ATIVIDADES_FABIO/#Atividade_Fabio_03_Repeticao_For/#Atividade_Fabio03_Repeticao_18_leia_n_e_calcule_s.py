#entrada e processamento

def fracao ():
    n = int(input("N: "))
    numerador = 1
    denominador = n
    somatorio = 0

    while n >= 1:
       somatorio = somatorio + (numerador/denominador)
       numerador += 1
       denominador -= 1
       n -= 1 
    
    print("Somatorio:",somatorio)


#saida

fracao()