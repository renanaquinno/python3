#entrada
habitantes = int(input("Quantos habitantes: "))
contador = 0
media_salarial = 0
media_filhos = 0
ate_mil = 0

#processamento

def senso (habitantes, contador, media_salarial, media_filhos, ate_mil):
    while contador < habitantes:
        salario = float(input("Salario: "))
        filhos = int(input("N. de filhos: "))
        media_salarial += salario
        media_filhos += filhos
        contador += 1
        if salario <= 1000:
            ate_mil += 1
    media_salarial = round(media_salarial / habitantes)
    media_filhos = round(media_filhos / habitantes)
    print(f"MÉDIA SALARIAL: {media_salarial}\nMEDIA DE FILHOS: {media_filhos}\nATE MIL REAIS: {ate_mil}")       

senso(habitantes, contador, media_salarial, media_filhos, ate_mil)


