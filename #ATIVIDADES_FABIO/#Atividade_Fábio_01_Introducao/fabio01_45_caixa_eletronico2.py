# Entrada
print("NÃO UTILIZE VALORES TERMINADOS EM 6 E 8\n")
saque = int(input("Informe o valor que sera sacado: "))

# Processamento
nota_100 = saque // 100
resto_100 = saque % 100
nota_50 = resto_100 // 50
resto_50 = resto_100 % 50
nota_20 = resto_50 // 20
resto_20 = resto_50 % 20
nota_10 = resto_20 // 10
resto_10 = resto_20 % 10
nota_5 = resto_10 // 5
resto_5 = resto_10 % 5
nota_2 = resto_5 // 2


# Saída

print("Será sacado:")
print(nota_100, "nota(s) de 100 reais,")
print(nota_50, "nota(s) de 50 reais,")
print(nota_20, "nota(s) de 20 reais,")
print(nota_10, "nota(s) de 10 reais,")
print(nota_5, "nota(s) de 5 reais e") 
print(nota_2, "nota(s) de 2 reais")