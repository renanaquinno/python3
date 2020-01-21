def emprestimo ():
    total = 3000
    dia = 0    
    while total > 0:
        total = (total * 0.0085) + total
        total = total - 200
        dia += 1
    print(dia)


emprestimo()