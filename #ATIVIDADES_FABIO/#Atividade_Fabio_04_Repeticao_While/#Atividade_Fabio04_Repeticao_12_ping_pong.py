#entrada
jogador1 = 0
jogador2 = 0


#processamento

def ping_pong (jogador1, jogador2):
    while jogador1 < 21 and jogador2 < 21:
        pontos = int(input("JOGADOR 1 OU 2: "))
        if pontos == 1:
            jogador1 += 1
        elif pontos == 2:
            jogador2 += 1
    if jogador1 == 21 and (jogador1 - jogador2) >=2:
        print("JOGADOR 1 GANHOU A PARTIDA")
    elif jogador2 == 21 and (jogador2 - jogador1) >=2:
        print("JOGADOR 2 GANHOU A PARTIDA")
    elif jogador1 > 21 and jogador2 > 21:
        if jogador1 - jogador2 >= 2:
            print("JOGADOR 1 GANHOU A PARTIDA")
        elif jogador2 - jogador1 >= 2:
            print("JOGADOR 2 GANHOU A PARTIDA")  



        
#saida

ping_pong(jogador1, jogador2)
