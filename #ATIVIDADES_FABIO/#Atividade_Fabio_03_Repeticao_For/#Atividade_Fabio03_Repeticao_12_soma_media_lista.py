
#entrada e processamento

def lista ():
    n = int(input("Informe N: "))
    lista_n = int(input("Informe quantos numeros tera a lista: "))
    contador = 0
    soma = 0
    media = 0

    while contador < lista_n:          
        n = int(input("Informe N: "))
        soma += n
        contador += 1
    
    media = soma / lista_n
    print(f"Soma é {soma} e a Média {media}")        
            
        
    
#saida

lista()