# Entrada

anos = int(input("Informe a idade: "))
meses = int(input("Informe os meses?: "))
dias = int(input("Informe os dias?: "))

# Processamento
ano = anos * 365
mes = meses * 30
total = ano + mes + dias

# Saída
print("Aproximadamente", total, "dias de vida")