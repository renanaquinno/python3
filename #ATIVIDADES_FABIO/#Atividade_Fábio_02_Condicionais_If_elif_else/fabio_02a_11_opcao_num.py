#entrada 

opcao = int(input("ESCOLHA UM NÚMERO PARA OPÇÃO 1,2 OU 3: "))
num1 = int(input("DIGITE UM VALOR PARA NUM1: "))
num2 = int(input("DIGITE UM VALOR PARA NUM2: "))
num3 = int(input("DIGITE UM VALOR PARA NUM3: "))


#processamento

def opcao_num ():
    if opcao == 1:
        print(num1)
    elif opcao == 2:
        print(num2)
    elif opcao == 3:
        print(num3)
    else:
        print("VOCE ESCOLHEU UM NÚMERO INVÁLIDO PARA OPÇÃO")


#saida

opcao_num ()