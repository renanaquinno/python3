#entrada

salario = float(input())


#processamento

def novo_salario (salario):
    if salario > 0 and salario <= 400:
        percentual = 0.15
        reajuste = salario * percentual
        salario_novo = reajuste + salario
    elif salario > 400 and salario <= 800:
        percentual = 0.12
        reajuste = salario * percentual
        salario_novo = reajuste + salario
    elif salario > 800 and salario <= 1200:
        percentual = 0.10
        reajuste = salario * percentual
        salario_novo = reajuste + salario
    elif salario > 1200 and salario <= 2000:
        percentual = 0.07
        reajuste = salario * percentual
        salario_novo = reajuste + salario
    else:
        percentual = 0.04
        reajuste = salario * percentual
        salario_novo = reajuste + salario
    
    print(f"Novo salario: {salario_novo:.2f} \nReajuste Ganho {reajuste:.2f} \nEm Percentual {percentual:.2f}%")
 
 
   
    
#saida   

novo_salario(salario)
    
        