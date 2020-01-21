#entrada e processamento

def salario_bonus ():
    nome = str(input())
    salario = float(input())
    bonus = float(input())
    bonus = bonus * 0.15
    salario = salario + bonus
    print("TOTAL = R$ {:.2f}".format(salario))

#saida

salario_bonus()