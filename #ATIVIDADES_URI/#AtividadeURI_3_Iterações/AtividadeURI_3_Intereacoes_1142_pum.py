#entrada

n = int(input())
contador = 1


# processamento

def quadrado_cubo (n, contador):
    numero = 1
    while contador <= n:
        print(numero, numero+1, numero+2,"PUM")
        contador += 1
        numero += 4



#saida

quadrado_cubo(n, contador)