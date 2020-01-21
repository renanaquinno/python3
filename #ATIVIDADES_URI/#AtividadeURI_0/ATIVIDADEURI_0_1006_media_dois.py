#entrada e #processamento

def nota ():
    a = float(input())
    b = float(input())
    c = float(input())
    peso_um = 2
    peso_dois = 3
    peso_tres = 5
    media = ((a * peso_um) + (b * peso_dois) + (c * peso_tres)) / 10
    print("MEDIA = {:.1f}".format(media))


#saida

nota()s