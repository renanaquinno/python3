#entrada

senha = 0000


#processamento

def senha_fixa (senha):
    while senha != 2002:
        senha = int(input())
        if senha != 2002:
            print("Senha Invalida")
        else:
            print("Acesso Permitido")
            break

#saida

senha_fixa(senha)