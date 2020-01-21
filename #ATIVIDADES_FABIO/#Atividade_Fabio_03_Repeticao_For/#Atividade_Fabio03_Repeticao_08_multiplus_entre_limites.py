#entrada e processamento

def multiplus ():
    n = int(input("Informe N: "))
    limite_inferior = int(input("Informe Limite Inf.: "))
    limite_superior = int(input("Informe Limite Sup.: "))
    contador = limite_inferior
    multiplo = n
    n_natural = n

    while contador < limite_superior: 
        if multiplo < limite_inferior:           
            print(multiplo + limite_inferior)
            multiplo = n * n_natural 
            n += 1
            contador = multiplo
        else:           
            print(multiplo)
            multiplo = n * n_natural
            n += 1
            contador = multiplo
        
    
#saida

multiplus()