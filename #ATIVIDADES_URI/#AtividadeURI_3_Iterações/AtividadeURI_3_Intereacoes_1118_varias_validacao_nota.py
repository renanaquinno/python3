#entrada



# processamento

def nota_valida ():
    novamente = 1
    while novamente == 1:
        x = float(input())
        while x < 0 or x > 10:
            print("nota invalida")
            x = float(input())
        y = float(input())
        while y < 0 or y > 10:
            print("nota invalida")
            y = float(input())
        
        media = (x+y)/2
        print("media = {:.2f}".format(media))
        novamente = int(input("novo calculo (1-sim 2-nao)"))
        while novamente != 1 and novamente != 2:
            novamente = int(input("novo calculo (1-sim 2-nao)"))

    
#saida

nota_valida()