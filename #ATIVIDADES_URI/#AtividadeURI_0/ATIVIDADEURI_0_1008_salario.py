#entrada e processamento

def salario ():
    numero = int(input())
    h_trabalhadas = int(input())
    valor_hora = float(input())
    salary = h_trabalhadas * valor_hora
    print("NUMBER =",numero)
    print("SALARY = U$ {:.2f}".format(salary))

#saida

salario()