#entrada

entrada = input()
dados = entrada.split()

#processamento
def sort ():
    a = int(dados[0])
    b = int(dados[1])
    c = int(dados[2])
    if a < b > c:
        maior = b
        if a > c:
            menor = c
            medio = a
        else:
            menor = a
            medio = c        
    elif b < a > c:
        maior = a
        if b > c:
            menor = c
            medio = b
        else:
            menor = b
            medio = c
    elif b < c > a:
        maior = c    
        if b > a:
            menor = a
            medio = b
        else:
            menor = b
            medio = a
    
        
    print(menor)
    print(medio)
    print(maior)
    print()
    print(a)
    print(b)
    print(c)

sort()