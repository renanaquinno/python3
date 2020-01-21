# Entrada
num = int(input("Escreva um número de 3 dígitos: "))

# Processamento
cent = num // 100
rest = num % 100
dezen = rest // 10
uni = rest % 10
num2 = uni*100 + dezen*10 + cent*1
total = num + num2

# Saída
print("A soma entre o número e seu inverso é:", total)