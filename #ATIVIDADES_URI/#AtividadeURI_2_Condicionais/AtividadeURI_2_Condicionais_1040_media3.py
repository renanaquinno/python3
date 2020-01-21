#entrada
entrada = input()
dados = entrada.split()

def calculos (dados):
    n1 = float(dados[0])
    n2 = float(dados[1])
    n3 = float(dados[2])
    n4 = float(dados[3])
    media = ((n1*2)+(n2*3)+(n3*4)+(n4*1)) / 10
    if media >= 7:
        situacao = "Aluno aprovado."
    elif media < 5:
        situacao = "Aluno reprovado."
    elif media >= 5 and media <= 6.9:
        situacao = "Aluno em exame."
       
    if situacao == "Aluno em exame.":
        print("Media: {:.1f}\n{}".format(media,situacao))
        exame = float(input())
        final = (media + exame) / 2
        if final >= 5:
            situacao = "Aluno aprovado."
        elif final <= 4.9:
            situacao = "Aluno reprovado."
        print("Nota do exame: {:.1f}\n{}\nMedia final: {:.1f}".format(exame,situacao,final))
    else:        
        print("Media: {:.1f}\n{}".format(media,situacao))

calculos(dados)