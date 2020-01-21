#entrada
n = int(input("Informe um Numero: "))
numeros = 0

#processamento
def main (n, numeros):
    if numeros == n:
        pass
    else:
        print(numeros+2)
        main(n,numeros+2)


#saida
main(n, numeros)