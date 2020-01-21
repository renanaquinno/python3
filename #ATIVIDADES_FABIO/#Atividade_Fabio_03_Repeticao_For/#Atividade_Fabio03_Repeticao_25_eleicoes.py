#entrada e processamento 
def eleicoes ():
    eleitores = int(input("N. de eleitores: "))
    contador = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while contador < eleitores:
        contador += 1
        voto = int(input("Voto: "))
        
        while voto != 1 and voto != 2 and voto != 3 and voto != 9 and voto!= 0:
            voto = int(input("Seu voto não é valido (Vote em 1,2,3,9 ou 0): "))
        
        if voto == 1:
            a += 1
        elif voto == 2:
            b += 1
        elif voto == 3:
            c += 1 
        elif voto == 9:
            d += 1
        elif voto == 0:
            e += 1
    
    print("Votos para:")
    print("Candidato A",a)
    print("Candidato B",b)
    print("Candidato C",c)
    print("Votos Nulos",d)
    print("Votos Brancos",e)
    
    if a > b and a > c:
        print("Candidato A venceu")
    elif b > a and b > c:
        print("Candidato B venceu")
    elif c > a and c > b:
        print("Candidato C venceu")


eleicoes()    