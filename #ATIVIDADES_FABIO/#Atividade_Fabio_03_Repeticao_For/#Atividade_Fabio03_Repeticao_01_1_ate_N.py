#entrada
n = int(input("Informe um Numero: "))
numeros = 0

#processamento
def main (n, numeros):
    if numeros == n:
        pass
    else:
        print(numeros+1)
        main(n,numeros+1)


#saida
main(n, numeros)