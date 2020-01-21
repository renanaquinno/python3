#entrada

matricula = 1


#processamento

def informacao_aluno (matricula):
    matricula = int(input("Numero de Matricula: "))
    aprovados = 0
    reprovados = 0
    alunos = 0
    while matricula != 0:
        nota_um = int(input("Nota um: "))
        nota_dois = int(input("Nota dois: "))
        nota_tres = int(input("Nota tres: "))
        media_final = (2*nota_um)+(3*nota_dois)+(5*nota_tres)/10
        if media_final >= 7:
            aprovados +=1
        elif media_final < 7:
            reprovados +=1
        alunos +=1
        matricula = int(input("Numero de Matricula: "))

    print("TOTAL DE APROVADOS: ",aprovados)
    print("TOTAL DE REPROVADOS: ",reprovados)
    print("TOTAL DE ALUNOS: ",alunos)
        


#saida

informacao_aluno(matricula)
