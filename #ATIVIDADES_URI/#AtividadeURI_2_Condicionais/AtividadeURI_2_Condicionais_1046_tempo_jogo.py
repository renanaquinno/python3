#entrada
entrada = input()
dados = entrada.split()


#processamento

def tempo_jogo (dados):
    hora_inicio = int(dados[0])
    hora_final = int(dados[1])    
    if hora_final > hora_inicio:
        duracao = hora_final - hora_inicio
    else:
        duracao = 24 - hora_inicio + hora_final
    print("O JOGO DUROU {} HORA(S)".format(duracao))


#saida

tempo_jogo(dados)