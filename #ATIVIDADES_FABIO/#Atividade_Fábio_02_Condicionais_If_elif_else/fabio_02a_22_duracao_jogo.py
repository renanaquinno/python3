#entrada

hora_inicio = int(input("DIGITE A HORA DO INÍCIO DO JOGO: "))
min_inicio = int(input("DIGITE OS MINUTOS DO INÍCIO DO JOGO: "))
hora_termino = int(input("DIGITE A HORA DO TERMINO DO JOGO: "))
min_termino = int(input("DIGITE OS MINUTOS DO TERMINO DO JOGO: "))


#processamento

def principal ():
    if hora_inicio >= hora_termino:
        outro_dia()
    elif hora_inicio < hora_termino:
        mesmo_dia()


def mesmo_dia ():
    if hora_inicio <= hora_termino:
        hora_duracao = hora_termino - hora_inicio
    if min_inicio > min_termino:
        min_duracao = min_termino - min_inicio + 60
        print(f"O JOGO DUROU {hora_duracao} HORAS E {min_duracao} MINUTOS")
    else:
        min_duracao = min_termino - min_inicio
        print(f"O JOGO DUROU {hora_duracao} HORAS E {min_duracao} MINUTOS")


def outro_dia ():
    hora_duracao = hora_termino - hora_inicio + 24     
    if min_inicio >= min_termino:
        min_duracao =  min_termino - min_inicio + 60  
        print(f"O JOGO DUROU {hora_duracao} HORAS E {min_duracao} MINUTOS")
    else:
        min_duracao = min_termino - min_inicio
        print(f"O JOGO DUROU {hora_duracao} HORAS E {min_duracao} MINUTOS")

#saida 

principal()
