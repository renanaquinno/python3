#entrada

lado_um = int(input("DIGITE A MEDIDA DO LADO UM: "))
lado_dois = int(input("DIGITE A MEDIDA DO LADO DOIS: "))
lado_tres =int(input("DIGITE A MEDIDA DO LADO TRES: "))
#processamento

def lados ():
    if lado_um > lado_dois and lado_um > lado_tres:
        hipotenusa = lado_um
        print(f"A HIPOTENUSA É {lado_um} E OS CATETOS SÃO {lado_dois} E {lado_tres}")
    elif lado_dois > lado_um and lado_dois > lado_tres:
        hipotenusa = lado_dois
        print(f"A HIPOTENUSA É {lado_dois} E OS CATETOS SÃO {lado_um} E {lado_tres}")  
    elif lado_tres > lado_um and lado_tres > lado_dois:
        hipotenusa = lado_tres
        print(f"A HIPOTENUSA É {lado_tres} E OS CATETOS SÃO {lado_um} E {lado_dois}")
#saida 

lados()
