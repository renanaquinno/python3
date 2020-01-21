#processamento

def eleicoes ():
    dilma = 0
    serra = 0
    ciro = 0
    indeciso = 0
    outros = 0
    brancos = 0
    voto = 0
    eleitores = 0
    while voto != -1:
        voto = int(input("Voto: "))
        if voto == 45:
            serra += 1
        elif voto == 13:
            dilma += 1
        elif voto == 23:
            ciro += 1
        elif voto == 99:
            indeciso += 1
        elif voto == 98:
            outros += 1
        elif voto == 0:
            brancos += 1
        
        eleitores += 1
        


    serra_turno = ((100 / eleitores) * serra)
    dilma_turno = ((100 / eleitores) * dilma)
    ciro_turno = ((100 / eleitores) * ciro)

    if serra_turno > dilma_turno > ciro_turno:
        segundo_turno = "DILMA E SERRA"
    elif dilma_turno > ciro_turno > serra_turno:
        segundo_turno = "DILMA E CIRO"
    elif ciro_turno > serra_turno > dilma_turno:
        segundo_turno = "CIRO E SERRA"

    print("SERRA: {:.2f} %".format((100 / eleitores) * serra))
    print("DILMA: {:.2f} %".format((100 / eleitores) * dilma))
    print("CIRO: {:.2f} %".format((100 / eleitores) * ciro))
    print("OUTROS: {:.2f} %".format((100 / eleitores) * outros))
    print("INDECISOS: {:.2f} %".format((100 / eleitores) * indeciso))
    print("BRANCOS: {:.2f} %".format((100 / eleitores) * brancos))
    print("ENTREVISTADOS: ",eleitores)
    
    if serra_turno > 50 or dilma_turno > 50 or ciro_turno > 50:
        pass
    else:
        print("TEM POSSIBILIDADE DE SEGUNDO TURNO ENTRE:", segundo_turno)

   
        


#saida

eleicoes()
