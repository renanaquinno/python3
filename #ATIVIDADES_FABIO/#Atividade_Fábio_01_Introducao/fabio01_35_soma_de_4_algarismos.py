# Entrada

num = int(input("Informe um número de 4 dígitos: "))

# Processamento

mil = num // 1000
resto = num % 1000
cent = resto // 100
rest_2 = resto % 100
dezen = rest_2 // 10 
unid = rest_2 % 10
total = mil + cent + dezen + unid

# Saída

print("A soma dos 4 algarismos é:", total)