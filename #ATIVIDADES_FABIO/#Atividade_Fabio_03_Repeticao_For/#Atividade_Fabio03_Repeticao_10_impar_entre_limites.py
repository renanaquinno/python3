
#entrada e processamento

def num_impares ():
    limite_inferior = int(input("Informe Limite Inf.: "))
    limite_superior = int(input("Informe Limite Sup.: "))
    impares = limite_inferior

    while impares < limite_superior: 
        if impares % 2 != 0:           
            print(impares)
            impares += 2
        else:
            impares += 1           
            print(impares)
                
    
#saida

num_impares()