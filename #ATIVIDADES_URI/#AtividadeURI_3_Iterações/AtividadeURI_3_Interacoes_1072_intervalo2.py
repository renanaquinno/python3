#entrada 
n = int(input())

#processamento

def valores (n):
    dentro = 0
    fora = 0
    contador = 0
    while contador < n:
        numeros = int(input())
        contador += 1
        if numeros >= 10 and numeros <=20:
            dentro += 1
        else:
            fora += 1
    print("{} in".format(dentro))
    print("{} out".format(fora))


#saida

valores(n)