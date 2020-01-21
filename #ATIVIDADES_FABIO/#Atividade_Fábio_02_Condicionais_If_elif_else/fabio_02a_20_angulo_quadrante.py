#entrada

angulo = float(input("DIGITE O ANGULO: "))



#processamento


def quadrante ():
    if angulo > 0 and angulo < 90:
        print(f"O SEU ÂNGULO DE {angulo} ESTA NO PRIMEIRO QUADRANTE")
    elif angulo > 90 and angulo < 180:
       print(f"O SEU ÂNGULO DE {angulo} ESTA NO SEGUNDO QUADRANTE")
    elif angulo > 180 and angulo < 270:
       print(f"O SEU ÂNGULO DE {angulo} ESTA NO TERCEIRO QUADRANTE")
    elif angulo > 270 and angulo <= 360:
        print(f"O SEU ÂNGULO DE {angulo} ESTA NO QUARTO QUADRANTE")
    else:
        print(f"{angulo} NAO É UM ANGULO VÁLIDO")


#saida

quadrante()