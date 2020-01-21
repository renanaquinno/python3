#entrada

n = int(input())
contador = 1


# processamento

def sequencia_logica (n, contador):
    um = 1
    dois = 1
    tres = 1
    subtrair = 0
    multiplica = 1
    multiplica_dois = 2
    multiplica_tres = 1
    while contador <= n:
        print(um, dois*multiplica, (um* (dois*multiplica)))
        print(um, (dois*multiplica_dois)-subtrair,1+(um* (dois*multiplica)))
        um += 1
        dois += 1
        tres += um * dois
        contador +=1
        multiplica +=1
        multiplica_dois +=1
        multiplica_tres +=1
        subtrair +=1


#saida

sequencia_logica(n, contador)