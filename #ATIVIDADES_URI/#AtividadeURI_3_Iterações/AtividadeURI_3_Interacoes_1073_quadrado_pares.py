#entrada

n = int(input())


#processamento

def main (n):
    numeros = 0
    while numeros < n:
        numeros += 2
        if numeros <= n:
            print("{}^2 = {}".format(numeros, numeros ** 2) )
        

#saida

main(n)