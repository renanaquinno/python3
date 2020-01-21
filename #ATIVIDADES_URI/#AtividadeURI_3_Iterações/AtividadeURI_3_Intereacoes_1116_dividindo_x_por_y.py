#entrada

n = int(input())


# processamento

def divisao (n):
    contador = 0
    while contador < n:
        contador += 1
        numeros = input().split()
        dividendo = int(numeros[0])
        divisor = int(numeros[1])
        if divisor == 0:
            print("divisao impossivel")
        else:
            resultado = dividendo / divisor 
            print("{:.1f}".format(resultado))

     
    
#saida

divisao(n)