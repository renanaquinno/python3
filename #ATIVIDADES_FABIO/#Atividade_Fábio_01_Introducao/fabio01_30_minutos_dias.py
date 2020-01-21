# Entrada

minut = int(input("Informe os minutos: "))

# Processamento

dia = minut // 1440
rest = minut % 1440
hrs = rest // 60
minu_total = rest % 60

# Saída

print("Esses minutos são equivalentes a", dia, "dias(s),", hrs, "hora(s) e", minu_total, "minuto(s)")