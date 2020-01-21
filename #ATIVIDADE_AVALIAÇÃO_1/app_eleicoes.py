from importacao import importar_coligacoes, importar_vereadores
from funcionalidades import total, lista_todos_coligacoes, lista_todos_vereadores
import os


def main():

    # listas vazias
    coligacoes = []
    vereadores = []

    # preencher listas com dados importados: lista de dicionarios
    inicializar_dados(coligacoes, vereadores)

    # opcoes FAKE, demonstracao apenas
    menu = "***** ELEIÇÕES TERESINA/2012 *****\n 1 - Total de Coligacoes\n 2 - Listar Coligacoes\n 3 - Listar Vereadores\n 4 - Total Votos Válidos\n 5 - Quociente Eleitoral\n 6 - Total Votos por Coligação\n 7 - Total de Vagas por Quociente Partidario\n 0 - Sair\n\nOpção: "

    # Loop do Menu de opcões

    opcao = -1
    while opcao != 0:
        # pedir nova opcao
        opcao = int(input(menu))

        # verificar opcao e invocar funcao responsável
        if opcao == 1:
            total(coligacoes)
        elif opcao == 2:
            lista_todos_coligacoes(coligacoes)
        elif opcao == 3:
            lista_todos_vereadores(vereadores)
        elif opcao == 4:
            total_votos_validos(vereadores)
        elif opcao == 5:
            quociente_eleitoral(vereadores)
        elif opcao == 6:
            total_votos_coligacoes(vereadores, coligacoes)
        elif opcao == 7:
            total_vagas_coligacoes(vereadores, coligacoes)
        else:
            print('Opcao Invalida!')

        # limpar a tela
        input('Enter para continuar...')
        os.system('clear')  # se Windows: 'cls'



def inicializar_dados(coligacoes, vereadores):

    # Importar dados
    dados_coligacoes = importar_coligacoes('dados/partidos_coligacoes_the_2012.csv')
    dados_vereadores = importar_vereadores('dados/candidatos_e_votos_vereador_THE_2012.csv')

    # Log
    print('Carregados {} coligacoes e {} vereadores'.format(
        len(dados_coligacoes), len(dados_vereadores)))

    # Organizar dados em matrizes de acordo com o solicitado
    # TODO: preencher 'coligacoes' e 'vereadores' com dados já organizados
    for linhas in dados_coligacoes:
        coligacao = {'coligacoes': linhas, 'total_votos': 0, 'qtd_vagas': 0, 'vagas_sobras': 0}
        coligacoes.append(coligacao)
    for linhas in dados_vereadores:
        vereador = {'nome': linhas[0], 'numero': linhas[1], 'partido': linhas[2], 'coligacao': linhas[3], 'total_votos': linhas[4]}
        vereadores.append(vereador)

    # Limpar a tela
    input('Enter para ir ao Menu...')
    os.system('clear')  # ou 'cls'

def total_votos_validos(vereadores):
    total_votos = 0
    for linhas in vereadores:
        total_votos += int(linhas['total_votos'])
    print("Total de Votos Válidos:",total_votos)        
    
def quociente_eleitoral(vereadores):
    total_votos = 0
    for linhas in vereadores:
        total_votos += int(linhas['total_votos'])
    quociente = total_votos // 29
    print("Quociente Eleitoral dessa eleição foi:",quociente)


def total_votos_coligacoes(vereadores, coligacoes):
    for i in coligacoes:
        total = 0
        for linhas in vereadores:
            if (i['coligacoes']) == (linhas['coligacao']):
                total += int(linhas['total_votos'])
        print(i['coligacoes'], "Teve",total,"Votos")


def total_vagas_coligacoes(vereadores, coligacoes):
    #Quociente
    total_votos = 0
    for linhas in vereadores:
        total_votos += int(linhas['total_votos'])
    quociente = total_votos // 29

    for i in coligacoes:
        total = 0
        for linhas in vereadores:
            if (i['coligacoes']) == (linhas['coligacao']):
                total += int(linhas['total_votos'])
        if total >= quociente:
            vagas = total // quociente
            vagas_sobra = total % quociente
            print(i['coligacoes'], "Teve",vagas,"vagas")


if __name__ == '__main__':
    main()
