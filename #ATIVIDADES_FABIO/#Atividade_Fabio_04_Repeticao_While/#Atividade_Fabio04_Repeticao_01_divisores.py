#entrada

quantidade = int(input())


#processamento

def divisores_flag (quantidade):
    contador = 0
    while contador < quantidade:
        numero = int(input())
        divisor = 1
        while divisor <= numero:
            if numero % divisor == 0:
                print("{} é divisor de {}".format(divisor, numero))
                divisor += 1
            else:
                divisor += 1

        contador += 1


#saida

divisores_flag(quantidade)
