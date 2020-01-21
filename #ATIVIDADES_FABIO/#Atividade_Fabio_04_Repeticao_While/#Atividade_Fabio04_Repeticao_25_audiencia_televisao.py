#processamento

def audiencia ():
    dois = 0
    quatro = 0
    cinco = 0
    sete = 0
    dez = 0
    voto = 1
    eleitores = 0
    while voto != 0:
        voto = int(input("Voto: "))
        if voto == 2:
            dois += 1
        elif voto == 4:
            quatro += 1
        elif voto == 5:
            cinco += 1
        elif voto == 7:
            sete += 1
        elif voto == 10:
            dez += 1
     
        
        eleitores += 1

  

    print("Canal 2: {:.2f} %".format((100 / eleitores) * dois))
    print("Canal 4: {:.2f} %".format((100 / eleitores) * quatro))
    print("Canal 5: {:.2f} %".format((100 / eleitores) * cinco))
    print("Canal 7: {:.2f} %".format((100 / eleitores) * sete))
    print("Canal 10: {:.2f} %".format((100 / eleitores) * dez))
    print("ENTREVISTADOS: ",eleitores)
      
        


#saida

audiencia()
