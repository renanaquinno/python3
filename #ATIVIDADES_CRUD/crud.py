import random

class Cadastro:
    def __init__(self):
        self.__montadora = input('Digite montadora: ')
        self.__pais = input('Digite a pais: ')
        self.__codigo = self.__gerar_codigo()

    def __repr__(self):
        return "--- Cadastro de Montadoras ---\n Montadora : {}\n País: {}\n Código: {}".format(
        self.__montadora, self.__pais, self.__codigo
    )

    def __gerar_codigo(self):
        return int(input('Digite o Código: '))

    @property
    def montadora(self):
        return self.__montadora

    @property
    def pais(self):
        return self.__pais

    @property
    def codigo(self):
        return self.__codigo


class cadastro_veiculo:
    def __init__(self):
        self.__modelo = input('Digite o Modelo: ')
        self.__cor = input('Digite a cor   : ')
        self.__placa = self.__gerar_placa()

    def __repr__(self):
        return "\n--- Cadastro de Veículos ---\n Modelo : {}\n Cor: {}\n Placa: {}".format(
        self.__modelo, self.__cor, self.__placa
    )

    def __gerar_placa(self):
        return input('Digite a placa: ')

    @property
    def modelo(self):
        return self.__modelo

    @property
    def cor(self):
        return self.__cor

    @property
    def placa(self):
        return self.__placa 

opcao = 0
codigos = {}

while opcao != 9:
    opcao = int(input('\n\nCadastrar -- digite 1\nConsultar -- digite 2 \nPara sair -- digite 3\nOpção: '))

    if opcao == 1:
        while opcao != 0:
            opcao = int(input('\nCadastrar Montadora: -- digite 1\nCadastrar Veículo  : -- digite 2 \nVoltar Anterior    : -- digite 0\nOpção: '))
            if opcao == 1:
                print('\n\nCadastrando nova Montadora...')
                cadastro_novo = Cadastro()
                codigos[cadastro_novo.codigo] = cadastro_novo
                print(cadastro_novo)
            elif opcao == 2:
                print('\n\nCadastrando novo Veículo...')
                cadastro_novo = cadastro_veiculo()
                codigos[cadastro_novo.placa] = cadastro_novo
                print(cadastro_novo)
            elif opcao == 0:
                print('\nVoltando...')

    elif opcao == 2:
        codigo = int(input('\n\nDigite o Código: '))
        if codigo in codigos.keys():
            print(codigos[codigo])
        else:
            print('Código #{} não existe.'.format(codigo))
    elif opcao == 9:
        print('\n\nSaindo.')
    else:
        print('\n\nOpcao invalida.')