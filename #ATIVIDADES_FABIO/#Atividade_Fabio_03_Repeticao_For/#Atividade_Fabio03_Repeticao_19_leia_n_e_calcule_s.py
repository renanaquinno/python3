#entrada e processamento

def fracao ():
    n = int(input("N: "))
    item_a = 0
    item_b = n
    contador = 1
    somatorio = 0

    while contador <= n:
        
        if contador % 2 != 0:
            item = item_a / item_b
            somatorio += item
            print("+ {}/{}".format(item_a, item_b))
        else:
            item = item_b / item_a
            somatorio -= item
            print("- {}/{}".format(item_b, item_a))               
        
        item_a += 1
        item_b -= 1
        contador += 1 

    print("Somatorio:",somatorio)
    
    
#saida

fracao()