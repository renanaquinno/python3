#entrada

angulo_um = int(input("INFORME O PRIMEIRO ANGULO: "))
angulo_dois = int(input("INFORME O SEGUNDO ANGULO: "))
angulo_tres = int(input("INFORME O TERCEIRO ANGULO: "))


#processamento

def triangulo ():
    if angulo_um == 0 or angulo_dois == 0 or angulo_tres == 0:
        print("NÃO EXISTE TRIANGULO COM ANGULO 0")
    elif angulo_um + angulo_dois + angulo_tres > 180:
        print("ISSO É MAIOR QUE TRIANGULO")
    elif angulo_um + angulo_dois + angulo_tres < 180:
        print("ISSO É MENOR QUE TRIANGULO")
    elif angulo_um + angulo_dois + angulo_tres == 180:
        if angulo_um < 90 and angulo_dois < 90 and angulo_tres < 90:
            print("TRIANGULO ACUTÂNGULO")
        elif angulo_um == 90 or angulo_dois == 90 or angulo_tres == 90:
            print("TRIANGULO RETANGULO")
        elif angulo_um or angulo_dois or angulo_tres > 90:
            print("TRIANGULO OBTUSÂNGULO")


#saida

triangulo()