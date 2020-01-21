#entrada

x = -1
y = -1


# processamento

def nota_valida (x, y):
    while x < 0 or x > 10:
        x = float(input())
        if x < 0 or x > 10:
            print("nota invalida")
    while y < 0 or y >0:
        y = float(input())
        if y < 0 or y > 10:
            print("nota invalida")
        else: 
            media = (x+y)/2
            print("media = {:.2f}".format(media))
            break
    
#saida

nota_valida(x, y)