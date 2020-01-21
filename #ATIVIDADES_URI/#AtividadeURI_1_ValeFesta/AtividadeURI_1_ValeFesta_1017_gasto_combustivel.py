#processamento

def main():
    tempo_h = float(input())
    velocidade_media = float(input())
    distancia = tempo_h * velocidade_media
    gasolina = distancia / 12
    print("{:.3f}".format(gasolina))


#saida
	
main ()