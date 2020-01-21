#entrada

numero = int(input("Informe o Numero: "))


#processamento

def divisao (numero):
    while numero > 1:
        numero = numero / 2
    print(numero)

divisao(numero)