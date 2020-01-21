#entrada

nota_um = float(input("INFORME A PRIMEIRA NOTA: "))
nota_dois = float(input("INFORME A SEGUNDA NOTA: "))


#processamento

media = (nota_um + nota_dois) / 2

def media_prova ():
    if media > 6:
        print("APROVADO")
    elif (media + nota_um + nota_dois) / 3 > 4:
        print("APROVADO")
    else:
        print("REPROVADO")

#saida

media_prova()