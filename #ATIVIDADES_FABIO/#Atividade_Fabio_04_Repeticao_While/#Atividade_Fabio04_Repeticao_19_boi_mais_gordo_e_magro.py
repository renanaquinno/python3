#entrada e processamento

def fichas ():
    num_id = 1
    maior = 0
    maior = 0
    menor = 100000
    while num_id != 0:
        num_id = int(input("N. da Ficha: "))    
        if num_id != 0:
            peso = float(input("Peso do Boi: "))  
            if peso > maior:
                maior = peso
                identificacao_maior = num_id
            if peso < menor:
                menor = peso
                identificacao_menor = num_id          
            
        
        
    
    print(f"O BOI MAIS MAGRO É O {identificacao_menor} PESANDO {menor} KG")
    print(f"O BOI MAIS GORDO É O {identificacao_maior} PESANDO {maior} KG")
   
        
    
#saida

fichas()