# Entrada


seg = float(input("Informe os segundos: "))

# Processamento

hora = seg // 3600
rest = seg % 3600
minu = rest // 60
segundos = rest % 60

# Saída

print("Isso equivale a",hora,"horas(s),",minu,"minuto(s) e", segundos, "segundo(s)" )