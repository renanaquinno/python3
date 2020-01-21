#entrada

numero = int(input("Informe um Numero: "))
fat = 1
i = 2

#processamento

def fatorial (numero, fat, i):
    while i <= numero:
        fat = fat*i
        i = i+1
    print(fat)


#saida

fatorial(numero, fat, i)