# Entrada
a = int(input("Informe o valor de A?: "))
b = int(input("Informe o valor de B?: "))
c = int(input("Informe o valor de C?: "))
d = int(input("Informe o valor de D?: "))
e = int(input("Informe o valor de E?: "))
f = int(input("Informe o valor de F?: "))

# Processamento
x = (c*e) - (b*f) / (a*e) - (b*d)
y = (a*f) - (c*d) / (a*e) - (b*d)

# Saída
print("O valor de x é:", x, "e o valor de y é:", y)
