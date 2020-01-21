# Entrada

print("Esse programa irá mostrar o custo ao consumidor de um carro novo\n")
fabrica = float(input("Informe o valor de um carro na fábrica?: "))

# Processamento

distribuidor = fabrica * 0.28
impostos = fabrica * 0.45
custo_total = fabrica + distribuidor + impostos

# Saída

print("O valor do carro para o consumidor é:", custo_total)
