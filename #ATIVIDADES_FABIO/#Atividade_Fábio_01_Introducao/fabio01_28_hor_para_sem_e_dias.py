
#entrada
horas = int(input("Informe o número em horas "))

#processamento 
sem = horas // 168
dias = horas % 168
hora = horas // 24

#saida
print("A quantidade de horas equivalem a",sem,"semana(s)",dias,"dia(s) e",hora,"horas")
