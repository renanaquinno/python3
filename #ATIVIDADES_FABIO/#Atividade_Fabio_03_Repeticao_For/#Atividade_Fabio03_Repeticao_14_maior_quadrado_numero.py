
#entrada e processamento

def quadrado_maior ():
    n = int(input("Informe N: ")) 
    quadrado = 1
    numero = 1

    while quadrado < n:          
        quadrado = numero * numero
        numero += 1         
        
    quadrado = (numero-2) * (numero-2)
    print(quadrado)
        
    
#saida

quadrado_maior()