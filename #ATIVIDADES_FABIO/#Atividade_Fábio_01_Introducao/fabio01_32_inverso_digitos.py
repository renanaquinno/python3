# Entrada
num = int(input("Informe um número de 3 dígitos: "))

# Processamento

cent = num // 100
rest = num % 100
dezen = rest // 10
uni = rest % 10
new_num = uni*100 + dezen*10 + cent*1
total = num - new_num

# Saída

print("A diferença entre o número e seu inverso é:", total)