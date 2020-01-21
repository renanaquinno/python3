from importacao import importar_coligacoes, importar_vereadores

def main():
    dados_coligacoes = importar_coligacoes('dados/partidos_coligacoes_the_2012.csv')
    dados_vereadores = importar_vereadores('dados/candidatos_e_votos_vereador_THE_2012.csv')

    # Log
    print('Carregados {} coligacoes e {} vereadores'.format(
        len(dados_coligacoes), len(dados_vereadores)))

    # Organizar dados em matrizes de acordo com o solicitado
    # TODO: preencher 'coligacoes' e 'vereadores' com dados já organizados
    for i in dados_coligacoes:
        print(i) 

main()