#entrada

numero = int(input("DIGITE UM NUMERO DE 0 A 100: "))


#processamento

def par_ou_impar ():
    if numero == 0:
        print("ZERO NÃO É IMPAR E NEM PAR")
    elif numero % 2 == 0:
        print("{} É UM NUMERO PAR".format(numero))
    else:
        print("{} É UM NUMERO IMPAR".format(numero))


#saida

par_ou_impar()