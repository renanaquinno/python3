# Entrada
binario = int(input("Informe o numero do binário: "))

# Processamento
milhar = binario // 1000
rest = binario % 1000
cent = rest // 100
rest_1 = rest % 100
dezen = rest_1 // 10
unid = rest_1 % 10

# Cálculo do binário
binario_1 = (2**0) * unid
binario_2 = (2**1) * dezen
binario_3 = (2**2) * cent
binario_4 = (2**3) * milhar
decimal = binario_1 + binario_2 + binario_3 + binario_4

# Saída
print("Equivale a", decimal, "em decimal")