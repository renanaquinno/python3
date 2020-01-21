#entrada

prof_um = int(input("INFORME O NÚMERO DE AULAS/HORAS DO PRIMEIRO PROFESSOR: "))
prof_dois = int(input("INFORME O NUMERO DE AULAS/HORAS DO SEGUNDO PROFESSOR: "))
salario_um = float(input("INFORME O VALOR DA AULA DO PRIMEIRO PROFESSOR: "))
salario_dois = float(input("INFORME O VALOR DA AULA DO SEGUNDO PROFESSOR: "))
total_um = 0
total_dois = 0


#processamento

total_um = prof_um * salario_um
total_dois = prof_dois * salario_dois

def salario_prof ():
    if total_um == total_dois:
        print("OS SALÁRIO SÃO IGUAIS DE R$ {}".format(total_um))
    elif total_um > total_dois:
        print("O PRIMEIRO PROFESSOR TEM UM SALARIO MAIOR, RECEBENDO R$ {}".format(total_um))
    else:
        print("O SEGUNDO PROFESSOR TEM UM SALÁRIO MAIOR, RECEBENDO R$ {}".format(total_dois))


#saida

salario_prof()