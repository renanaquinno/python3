#entrada e #processamento

def salario ():
    funcionarios = int(input("Quantidade de funcionários: "))
    contador = 0
    while contador < funcionarios:
        contador += 1
        codigo = int(input("Código: "))
        h_trabalho = int(input("Horas Trabalhadas: "))
        num_dependentes = int(input("Dependentes: "))
        salario_bruto = 12 * h_trabalho
        salario_bruto += (40 * num_dependentes)
        inss = salario_bruto * 0.085
        ir = salario_bruto * 0.05
        salario_liquido = salario_bruto - inss - ir
        print("INSS: {:.2f}".format(inss))
        print("IR: {:.2f}".format(ir))
        print("Salario líquido: {:.2f}".format(salario_liquido))


#saida
    
salario()
