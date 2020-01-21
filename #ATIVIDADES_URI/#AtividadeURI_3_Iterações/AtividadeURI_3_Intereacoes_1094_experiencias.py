#entrada

n = int(input())
contador = 1


# processamento

def experiencias (n, contador):
    rato = 0
    coelhos = 0
    sapo = 0
    while contador <= n:
        contador += 1
        valores = input().split()
        quantia = int(valores[0])
        tipo = valores[1]
        if tipo == "C":
            coelhos += quantia
        elif tipo == "R":
            rato += quantia
        elif tipo == "S":
            sapo += quantia

    cobaias = sapo + coelhos + rato
    print("Total: {} cobaias".format(cobaias))    
    print("Total de coelhos:", coelhos)    
    print("Total de ratos:", rato)    
    print("Total de sapos:", sapo)
    cobaias = 100 / cobaias
    coelhos = cobaias * coelhos    
    rato = cobaias * rato    
    sapo = cobaias * sapo    
    print("Percentual de coelhos: {:.2f} %".format(coelhos))
    print("Percentual de ratos: {:.2f} %".format(rato))
    print("Percentual de sapos: {:.2f} %".format(sapo))

    
        
#saida

experiencias(n, contador)