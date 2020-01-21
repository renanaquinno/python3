# Entrada

nota1 = float(input("Informe a primeira nota: "))
peso1 = float(input("Informe o peso que ela possui: "))
nota2 = float(input("Informe a segunda nota: "))
peso2 = float(input("Informe o peso que ela possui: "))
nota3 = float(input("Informe a terceira nota: "))
peso3 = float(input("Informe o peso que ela possui: "))

# Processamento

part_1 = (nota1*peso1) + (nota2*peso2) + (nota3*peso3)
part_2 = peso1 + peso2 + peso3
media = part_1 / part_2

# Saída

print("A média foi:",media, "pontos")