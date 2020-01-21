# Entrada

dias = int(input("Informe os dias de vida: "))

# Processamento

ano = dias // 365
resto = dias % 365
meses = resto // 12
resto2 = resto % 12
dia = resto2

# Saída
print("Aproximadamente", ano, "anos", meses, "meses e", dia, "dias")