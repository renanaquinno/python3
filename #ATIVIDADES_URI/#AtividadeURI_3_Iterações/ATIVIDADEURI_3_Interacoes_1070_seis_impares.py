#entrada e processamento

def num_impares ():
    limite_inferior = int(input())
    limite_superior = limite_inferior + 12
    impares = limite_inferior

    while impares < limite_superior: 
        if impares % 2 != 0:           
            print(impares)
        impares += 1
                  
    
#saida

num_impares()