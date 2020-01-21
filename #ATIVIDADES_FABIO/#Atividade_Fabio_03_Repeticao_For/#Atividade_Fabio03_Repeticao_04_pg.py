#entrada

from ferramentas import * 

#processamento

def main (n, numeros):
    inicio =  get_inteiro("Inicio: ")
    limite = get_inteiro"Limite: ", inicio)
    
    if limite > inicio:
        razao = get_inteiro_positivo("Razão: ")
    else:
        razao = get_inteiro_negativo("Razão: ")

    while (razao > 0 and inicio < limite) or (razao < 0 and inicio > limite):
        print(inicio, end=", ")
        inicio = inicio * razao


    print()


#saida
main(n, numeros)