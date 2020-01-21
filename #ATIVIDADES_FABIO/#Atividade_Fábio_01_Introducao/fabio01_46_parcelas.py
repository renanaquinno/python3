# Entrada
print("Esse programa irá mostrar um sitema de parcelamento divido em 3 suaves prestações\n")
val_prod = int(input("Informe o valor do produto: "))

# Processamento

entrada = val_prod // 3 + val_prod % 3
parcelas = (val_prod - entrada) / 2

# Saída

print("A entrada vai ser de", entrada, "Reais e as parcelas vão ser de", parcelas, "Reais")