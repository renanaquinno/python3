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

    contador = menor
    soma = 0

    while contador <= maior: 
        if contador % 13 != 0:           
            soma += contador
            contador += 1
        else:
            contador += 1
    
    print(soma)         
                
    
#saida

multiplos_13()