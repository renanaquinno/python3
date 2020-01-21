#entrada

numero_a = int(input())
numero_b = int(input())


#processamento

def multiplicacao (numero_a, numero_b):
    divisor = 0
    if numero_a > numero_b:
        maior = numero_a
        menor = numero_b
    else:
        maior = numero_b
        menor = numero_a
    
    resultado = maior

    while maior > 0:
        divisor += 1
        resultado -= menor 
        
    print("Quociente",divisor)
    prova = divisor * menor
    
    if prova > resultado:
        resto = prova - resultado
    elif prova < resultado:
        resto = resultado - prova

    
    print("Resto",resto)
        

#saida

multiplicacao(numero_a, numero_b)
