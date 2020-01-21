
#entrada e processamento
def num_pares ():
    limite_inferior = int(input("Informe Limite Inf.: "))
    limite_superior = int(input("Informe Limite Sup.: "))
    pares = limite_inferior

    while pares < limite_superior: 
        if pares % 2 == 0:           
            print(pares + 2)
            pares += 2 
        else:           
            print(pares +1)
            pares += 2
        
    
#saida
num_pares()