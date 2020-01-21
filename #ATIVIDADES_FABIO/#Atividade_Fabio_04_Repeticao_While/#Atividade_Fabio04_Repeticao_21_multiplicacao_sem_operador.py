#entrada

numero_a = int(input())
numero_b = int(input())


#processamento

def multiplicacao (numero_a, numero_b):
    multiplicador = 0
    resultado = 0
    if numero_a > numero_b:
        maior = numero_a
        menor = numero_b
    else:
        maior = numero_b
        menor = numero_a
    while multiplicador < maior:
        multiplicador += 1
        resultado += menor 

    print(resultado)
        

#saida

multiplicacao(numero_a, numero_b)
