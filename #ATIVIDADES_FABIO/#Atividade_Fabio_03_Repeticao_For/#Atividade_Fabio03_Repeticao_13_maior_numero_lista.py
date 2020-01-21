
#entrada e processamento

def lista ():
    n = int(input("Informe N: "))
    lista_n = int(input("Informe quantos numeros tera a lista: "))
    contador = 0
    maior = 0

    while contador < lista_n:          
        n = int(input("Informe N: "))
        contador += 1
        if n > maior:
            maior = n
        else:
            maior = maior
        
    
    print(maior)        
            
        
    
#saida

lista()