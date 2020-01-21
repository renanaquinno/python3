#entrada

salario = 1

#entrada

def salarios (salario):
    soma_salario_atual = 0
    soma_salario_novo = 0
    while salario != 0:
        salario = float(input("Salário: "))
        if salario < 3000:
            novo_salario = (salario * 0.25) + salario
            print("Novo Salario: R$", novo_salario)
            soma_salario_atual += salario
            soma_salario_novo += novo_salario
        elif salario < 6000:
            novo_salario = (salario * 0.20) + salario
            print("Novo Salario: R$", novo_salario)
            soma_salario_atual += salario
            soma_salario_novo += novo_salario
        elif salario < 10000:
            novo_salario = (salario * 0.15) + salario
            print("Novo Salario: R$", novo_salario)
            soma_salario_atual += salario
            soma_salario_novo += novo_salario
        elif salario >= 10000:
            novo_salario = (salario * 0.10) + salario
            print("Novo Salario: R$", novo_salario)
            soma_salario_atual += salario
            soma_salario_novo += novo_salario
    
    print("Soma salário atual:",soma_salario_atual)
    print("Soma salário novo:",soma_salario_novo)
    print("Diferenças salários:",soma_salario_novo - soma_salario_atual)

#saida

salarios(salario)