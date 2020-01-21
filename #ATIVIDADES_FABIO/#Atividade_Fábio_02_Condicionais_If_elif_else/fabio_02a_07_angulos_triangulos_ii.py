#entrada

angulo_um = int(input("INFORME O PRIMEIRO ANGULO: "))
angulo_dois = int(input("INFORME O SEGUNDO ANGULO: "))
angulo_tres = int(input("INFORME O TERCEIRO ANGULO: "))


#processamento e #saida

def angulos_triangulos ():
    if angulo_um == 0 or angulo_dois == 0 or angulo_tres == 0:
        print("NÃO EXISTE TRIANGULO COM ANGULO 0")
    elif angulo_um + angulo_dois < angulo_tres:
        print("ISSO NÃO É UM TRIANGULO")
    elif angulo_um + angulo_dois >= angulo_tres:
        if angulo_um == angulo_dois and angulo_um == angulo_tres:
            print("TRIANGULO EQUILATERO")
        elif angulo_um == angulo_dois or angulo_um == angulo_tres:
            print("TRIANGULO ISOSCELES")
        elif angulo_dois == angulo_tres:
            print("TRIANGULO ISOSCELES")
        elif angulo_um != angulo_dois and angulo_um != angulo_tres:
            print("TRIANGULO ESCALENO")


#saida

angulos_triangulos()