#entrada

m = 2
n = 2

# processamento

def sequencia (m, n):
    while m > 0 and n > 0:  
        valores = input().split()
        m = int(valores[0])
        n = int(valores[1])
        if m > 0 and n > 0:  
            if m > n:
                menor = n
                maior = m
            else:
                menor = m
                maior = n
            soma = menor
            print("{} " .format(menor), end="")
            while menor < maior:
                menor += 1
                soma += menor
                print("{} " .format(menor), end="")
            print("Sum={}".format(soma))
#saida

sequencia(m, n)