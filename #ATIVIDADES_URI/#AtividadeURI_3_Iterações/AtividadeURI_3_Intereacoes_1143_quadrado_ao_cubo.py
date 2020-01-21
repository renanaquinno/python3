#entrada

n = int(input())
contador = 1


# processamento

def quadrado_cubo (n, contador):
    while contador <= n:
        print(contador, contador*contador, contador**3)
        contador += 1


#saida

quadrado_cubo(n, contador)