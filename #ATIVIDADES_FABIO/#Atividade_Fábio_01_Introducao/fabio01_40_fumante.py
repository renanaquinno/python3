# Entrada
anos = int(input("Por quantos anos você fuma?: "))
num_cigarro = int(input("Quantos cigarros você fuma por dia?: "))
preco = float(input("Qual o preço de uma carteira de cigarros?: "))

# Processamento

anos_fumando = anos * 365
dinheiro_gasto = ((num_cigarro * anos_fumando) / 20) * preco

# Saída
print("Foram gastos", dinheiro_gasto, "reais em cigarro")