# Entrada
saque = int(input("Informe o valor que sera sacado: "))

# Processamento
nota_50 = saque // 50
resto_50 = saque % 50
nota_10 = resto_50 // 10
resto_10 = resto_50 % 10
nota_5 = resto_10 // 5
nota_1 = resto_10 % 5


# Saída
print("Será sacado:")
print(nota_50, "nota(s) de 50 reais,")
print(nota_10, "nota(s) de 10 reais,")
print(nota_5, "nota(s) de 5 reais e") 
print(nota_1, "nota(s) de 1 real")