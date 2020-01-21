#processamento

def dados ():
    pessoas = 0
    homem = 0
    mulher = 0
    idade_homem = 0
    idade_mulher = 0
    homem_solteiro = 0
    mulher_solteira = 0
    mulher_divorciada_trinta = 0
    while pessoas < 100:
        pessoas += 10
        sexo = int(input("Sexo - 1 para Homem ou 2 para Mulher: "))
        idade = int(input("Idade: "))
        estado_civil = int(input("Estado Civíl - 1 = Casado, 2 = Solteiro, 3 = Divorciado, 4 = Viúvo: "))
        if sexo == 1:
            idade_homem += idade
            homem += 1
            if estado_civil == 2:
                homem_solteiro += 1
        if sexo == 2: 
            idade_mulher += idade
            mulher += 1
            if estado_civil == 2:
                mulher_solteira += 1
            if estado_civil == 3:
                mulher_divorciada_trinta += 1
        
        
    idade_mulher = idade_mulher / mulher    
    idade_homem = idade_homem / homem
    homem_solteiro = homem / homem_solteiro     
    mulher_solteira = mulher / mulher_solteira  
       
    print("Idade Média Mulheres: {:.2f} anos".format(idade_mulher))
    print("Idade Média Homens: {:.2f} anos".format(idade_homem))

    print("Homens Solteiros: {:.2f} %".format(homem_solteiro))
    print("Mulheres Solteiras: {:.2f} %".format(mulher_solteira))
    
    print("Mulheres Divorciadas: {:.2f} ".format(mulher_divorciada_trinta))
      

#saida

dados()
