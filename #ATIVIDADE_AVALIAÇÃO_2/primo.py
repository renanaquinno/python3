#entrada

inicio = 10
fim = 1000


#processamento

def verifica_primos (inicio, fim):
    while inicio < fim:
        raiz_quadrada = int(inicio ** (1/2))
        
        while raiz_quadrada > 1:

            if inicio % raiz_quadrada == 0:
                raiz_quadrada = 1
            elif inicio % raiz_quadrada != 0:
                raiz_quadrada -= 1
                if raiz_quadrada == 1:
                    print(inicio)       
        inicio += 1 


#saida

verifica_primos(inicio, fim)