#entrada

valor_um = int(input("DIGITE O VALOR UM: "))
valor_dois = int(input("DIGITE O VALOR DOIS: "))
operacao = int(input("ESCOLHA UM OPERAÇÃO, DIGITANTO 1,2,3 OU 4: "))


#processamento

def adicao ():
    adicao = valor_um + valor_dois
    print(f"O RESULTADO DA ADIÇÃO É: {adicao}")
    
def subtracao ():
    if valor_um > valor_dois:
       subtracao = valor_um - valor_dois
       print(f"O RESULTADO DA SUBTRAÇÃO É: {subtracao}")
    else:
       subtracao = valor_dois - valor_um
       print(f"O RESULTADO DA SUBTRAÇÃO É: {subtracao}")
               
def multiplicacao ():
    multiplicacao = valor_um * valor_dois
    print(f"O RESULTADO DA MULTIPLICAÇÃO É: {multiplicacao}")

def divisao ():
    if valor_um > valor_dois:
        divisao = valor_um / valor_dois
        print(f"O RESULTADO DA DIVISÃO É: {divisao}")
    else:
        divisao = valor_dois / valor_um
        print(f"O RESULTADO DA DIVISÃO É: {divisao}")  

def operacoes ():
    if operacao == 1:
        adicao()
    elif operacao == 2:
        subtracao()
    elif operacao == 3:
        multiplicacao()
    elif operacao == 4:
        divisao()
    else:
        print("VOCE NAO ESCOLHEU UM NÚMERO VALIDO PARA OPERAÇÃO")


#saida

operacoes()