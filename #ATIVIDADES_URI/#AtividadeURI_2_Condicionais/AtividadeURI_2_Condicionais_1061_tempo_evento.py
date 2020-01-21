#entrada

dia_inicio = int(input("Dia "))
horario_inicio = input().split(":")
dia_final = int(input("Dia "))
horario_final = input().split(":")


#processamento
 
def evento (dia_inicio, horario_inicio, dia_final, horario_final):
     hora_inicio = int(horario_inicio[0])
     min_inicio = int(horario_inicio[1])
     seg_inicio = int(horario_inicio[2])

     hora_final = int(horario_final[0])
     min_final = int(horario_final[1])
     seg_final = int(horario_final[2])

     total_inicio = seg_inicio + (dia_inicio * 86400) + (hora_inicio * 3600) + (min_inicio *60)
     total_final = seg_final + (dia_final * 86400) + (hora_final * 3600) + (min_final *60) 

     horario_total = total_final - total_inicio

     dia_total = horario_total // 86400
     resto = horario_total - (dia_total * 86400)
     hora_total = resto // 3600
     resto = resto - (hora_total * 3600)
     min_total = resto // 60
     resto = resto - (min_total * 60)
     seg_total = resto // 1
     
     print("{} dia(s)".format(dia_total))
     print("{} hora(s)".format(hora_total))
     print("{} minuto(s)".format(min_total))
     print("{} segundo(s)".format(seg_total))


#saida

evento(dia_inicio, horario_inicio, dia_final, horario_final)