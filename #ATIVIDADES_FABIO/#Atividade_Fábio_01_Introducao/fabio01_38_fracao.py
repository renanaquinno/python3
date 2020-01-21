# Entrada
nume1 = int(input("Informe o numerador da Fração 1: "))
deno1 = int(input("Informe o denominador da Fração 1: "))
nume2 = int(input("Informe o numerador da Fração 2: "))
deno2 = int(input("Informe o denominador da Fração 2: "))

# Processamento

deno = deno1 * deno2
numerador = int(((deno / deno1) * nume1) + ((deno / deno2) * nume2))

# Saída

print("A soma das frações é aproximadamente ",numerador, "/", deno, sep="")