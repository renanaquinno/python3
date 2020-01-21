#entrada e processamento

def concurso ():
    nome = 1
    maior = 0
    maior = 0
    menor = 100000
    mais_baixa = 500
    mais_alta = 0
    while nome != "FIM":
        nome = input("Nome da candidata: ")
        if nome != "FIM":
            peso = float(input("Peso da Candidata: "))  
            altura = int(input("Altura da Candidata em cm: "))
            if peso > maior:
                maior = peso
                nome_gorda = nome
            if peso < menor:
                menor = peso
                nome_magra = nome
            if altura > mais_alta:
                mais_alta = altura
                nome_alta = nome
            if altura < mais_baixa:
                mais_baixa = altura
                nome_baixa = nome
                   
            
        
        
    print(f"A CANDIDATA MAIS ALTA É {nome_alta} MEDINDO {mais_alta} CM")
    print(f"A CANDIDATA MAIS BAIXA É {nome_baixa} MEDINDO {mais_baixa} CM") 
    print(f"A CANDIDATA MAIS MAGRA É {nome_magra} PESANDO {menor} KG")
    print(f"A CANDIDATA MAIS GORDA É {nome_gorda} PESANDO {maior} KG")
   
        
    
#saida

concurso()