#entrada e processamento

def num_impares ():
    x = int(input())
    y = int(input())
    
    if x > y:
        maior = x
        menor = y
    else:
        maior = y 
        menor = x

    impares = menor
    soma = 0

    while impares < maior: 
        if impares % 2 != 0:           
            if impares == menor:
                soma = 0
            else:
                soma += impares  
            impares += 2
        else:
            impares += 1   
    
    print(soma)         
                
    
#saida

num_impares()