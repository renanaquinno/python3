#entrada

numero = int(input("DIGITE UM NÚMERO DE 0 A 100: "))


#processamento

def numero_primo ():
    if numero == 2:
        print("O NUMERO É PRIMO")
    elif numero == 3:
        print("O NUMERO É PRIMO")
    elif numero == 5:
        print("O NUMERO É PRIMO")
    elif numero == 7:
        print("O NUMERO É PRIMO")
    elif numero % 2 == 0:
        print("O NUMERO NÃO É PRIMO")
    elif numero % 3 == 0:
        print("O NUMERO NÃO É PRIMO")
    elif numero % 5 == 0:
        print("O NUMERO NÃO É PRIMO")
    elif numero % 7 == 0:
        print("O NUMERO NÃO É PRIMO")
    else:
        print("O NUMERO É PRIMO")        
            

#saida

numero_primo()