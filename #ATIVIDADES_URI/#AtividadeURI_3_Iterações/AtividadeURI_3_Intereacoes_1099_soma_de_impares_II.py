#entrada

n = int(input())


# processamento

def num_impares (n):
    contador = 0
    while contador < n:
        contador += 1
        valores = input().split()
        x = int(valores[0])
        y = int(valores[1])
        
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

num_impares(n)