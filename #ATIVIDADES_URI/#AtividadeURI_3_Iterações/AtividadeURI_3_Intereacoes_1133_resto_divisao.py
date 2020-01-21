#entrada e processamento

def multiplos_13 ():
    x = int(input())
    y = int(input())
    
    if x > y:
        maior = x
        menor = y
    else:
        maior = y 
        menor = x

    contador = menor + 1
    soma = 0

    while contador < maior: 
        if contador % 5 == 2 or contador % 5 == 3:           
            print(contador)
            contador += 1
        else:
            contador += 1
    
                
    
#saida

multiplos_13()