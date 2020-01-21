#entrada

x = int(input("Informe o primeiro Numero: "))
n = int(input("Informe o segundo Numero: "))


#processamento

def calculo (x, n):   
    while n > 2:
        resultado = x / n
        print(f"{x}/{n}={resultado}")
        x = resultado 
        n -= 1


#saida

calculo(x, n)