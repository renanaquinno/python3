#inicio

n = int(input("Informe N: "))
contador = 1
soma = 0


#processamento

def soma_inteiros (n, contador, soma):
    while contador < n+1:
        soma += contador 
        contador += 1
    print(soma)


#saida

soma_inteiros (n, contador, soma)