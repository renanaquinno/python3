#entrada

dia_atual = int(input("INFORME O DIA DE HOJE: "))
mes_atual = int(input("INFORME O MÊS EM QUE ESTAMOS: "))
ano_atual = int(input("INFORME O ANO EM QUE ESTAMOS: "))
dia_nascimento = int(input("INFORME O DIA DE NASCIMENTO: "))
mes_nascimento = int(input("INFORME O MÊS DE NASCIMENTO: "))
ano_nascimento = int(input("INFORME O ANO DE NASCIMENTO: "))


#processamento

def idade_atual ():
    anos = ano_atual - ano_nascimento
    dia = dia_atual - dia_nascimento
    mes = mes_atual - mes_nascimento
    idade = ((mes * 30) + (anos * 365) + dia) // 365
    print("VOCÊ TEM {} ANOS".format(idade))


#saida

idade_atual()