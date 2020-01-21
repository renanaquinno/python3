
#entrada e processamento

def fracao ():
    n = int(input("Informe N: ")) 
    contador = 1
    denominador = 0
    denominador_comun = 1
    resultado = 0
    
    while contador < n+1:        
        denominador += 1
        denominador_comun = denominador * denominador_comun      
        contador += 1         
    while denominador > 0:
        resultado += denominador_comun / denominador
        denominador = denominador - 1

    print(resultado)
        
    
#saida

fracao()