#entrada

dados = input().split()


#processamento

def triangulo (dados):
    a = float(dados[0])
    b = float(dados[1])
    c = float(dados[2])
    if ((b - c) < a < (b + c)) and ((a - c) < b < (a + c)) and ((a - b) < c < (a + b)): 
        print("Perimetro = {:.1f}".format(a + b + c))
    else:
        print("Area = {:.1f}".format(((a + b) / 2) * c))

	
#saida

triangulo(dados)
