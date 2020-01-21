#entrada

n = int(input("Informe N: "))
m = int(input("Informe M: "))


#processamento 

def quadradro_perfeito (n, m):
    divisores = 1
    comparador = 0
    if n > m:
        maior = n
        menor = m
    else:
        maior = m
        menor = n

    while menor <= maior:
        divisores = 1
        comparador = 0
        while divisores < menor:
            if menor % divisores == 0:
                comparador += divisores
                divisores += 1
            elif menor % divisores != 0:
                divisores += 1  

        if comparador == menor:
            print(comparador, "É um quadrado perfeito")
        else:
            print(menor, "Não é um quadrado perfeito")
        menor += 1


#saida 
    
quadradro_perfeito (n, m)