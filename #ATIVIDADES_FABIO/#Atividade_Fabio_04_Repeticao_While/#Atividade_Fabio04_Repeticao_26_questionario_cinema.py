#processamento

def cinema ():
    otimo = 0
    bom = 0
    regular = 0
    pessimo = 0
    voto = 1
    idade = 0
    entrevistados = 0
    while idade != -1:
        idade = int(input("Idade: "))
        if idade != -1: 
            voto = int(input("Voto: "))
            idade += idade
            if voto == 1:
                otimo += 1
            elif voto == 2:
                bom += 1
            elif voto == 3:
                regular += 1
            elif voto == 4:
                pessimo += 1
        
            entrevistados += 1
            media_idade =  idade / entrevistados

    print("Idade Média: {:.2f} anos".format(media_idade))
    print("BOM: {:.2f} %".format((100 / entrevistados) * bom))
    print("ENTREVISTADOS: ",entrevistados)
      

#saida

cinema()
