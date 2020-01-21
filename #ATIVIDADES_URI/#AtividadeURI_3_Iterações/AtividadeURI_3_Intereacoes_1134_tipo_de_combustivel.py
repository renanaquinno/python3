#entrada 
combustivel = 0

#processamento

def tipo_combustivel (combustivel):
    alcool = 0
    gasolina = 0
    diesel = 0
    while combustivel != 4:
        combustivel = int(input())
        if combustivel == 1:
            alcool += 1
        elif combustivel == 2:
            gasolina += 1
        elif combustivel == 3:
            diesel += 1
        
    print("MUITO OBRIGADO")
    print("Alcool:" ,alcool)
    print("Gasolina:" ,gasolina)
    print("Diesel:", diesel)

#saida

tipo_combustivel(combustivel)