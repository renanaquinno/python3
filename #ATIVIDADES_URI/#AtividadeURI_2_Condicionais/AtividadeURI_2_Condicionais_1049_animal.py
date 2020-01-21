#processamento

dica_um = input()
dica_dois = input()
dica_tres = input()


def tipo (dica_um, dica_dois, dica_tres):
    if dica_um == "vertebrado":
        if dica_dois == "ave":
            if dica_tres == "carnivoro":
                print("aguia")
            elif dica_tres == "onivoro":
                print("pomba")
        elif dica_dois == "mamifero":
            if dica_tres == "onivoro":
                print("homem")
            elif dica_tres == "herbivoro":
                print("vaca")
    elif dica_um == "invertebrado":
        if dica_dois == "inseto":
            if dica_tres == "hematofago":
                print("pulga")
            elif dica_tres == "herbivoro":
                print("lagarta")
        elif dica_dois == "anelideo":
            if dica_tres == "hematofago":
                print("sanguessuga")
            elif dica_tres == "onivoro":
                print("minhoca")
                                            
    
tipo(dica_um, dica_dois, dica_tres)