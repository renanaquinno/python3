#entrada

dia = int(input("INFORME UM DIA: "))
mes = int(input("INFORME UM MÊS: "))
ano = int(input("INFORME UM ANO: "))


#processamento e #saida

def data_valida ():
    if dia < 0 and dia > 31:
        print("NÃO É UMA DATA VÁLIDA")
    elif mes < 0 and mes > 12:
        print("NÃO É UMA DATA VÁLIDA")
    elif ano < 0:
        print("NÃO É UMA DATA VÁLIDA")
    else:
        print("É UMA DATA VÁLIDA")

#saida

data_valida()