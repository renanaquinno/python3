
#entrada e processamento

def fichas ():
    n = int(input("Informe Numero de fichas: ")) 
    maior = 0
    menor = 0
    contador = 0
    identificacao_maior = 0
    identificacao_menor = 0
    while contador < n:
        num_id = int(input("N. da Ficha: "))
        nome = input("Nome do Boi: ")
        peso = float(input("Peso do Boi: "))
        if peso > maior:
            maior = peso
            identificacao_maior = num_id
        if peso < menor:
            menor = peso
            identificacao_menor = num_id          
        contador += 1
    
    print(f"O Maior boi é o {identificacao_maior} pesa {maior} KG\n e menor é o {identificacao_menor} pesando {menor} kg")
        
    
#saida

fichas()