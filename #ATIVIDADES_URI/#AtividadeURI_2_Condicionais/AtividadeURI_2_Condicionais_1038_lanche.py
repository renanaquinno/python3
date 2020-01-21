#entrada
entrada = input()
dados = entrada.split()
	
#processamento

def conta (dados):
    codigo = int(dados[0])
    quantidade = int(dados[1])
    if codigo == 1:
        total = quantidade * 4
    elif codigo == 2:
        total = quantidade * 4.50
    elif codigo == 3:
        total = quantidade * 5 
    elif codigo == 4:
        total = quantidade * 2
    elif codigo == 5:
        total = quantidade * 1.5            
    print("Total: R$ {:.2f}".format(total))

conta(dados)