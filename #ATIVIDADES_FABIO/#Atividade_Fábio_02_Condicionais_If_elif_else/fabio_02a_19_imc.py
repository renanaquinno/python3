#entrada

altura = float(input("DIGITE SUA ALTURA EM METROS: "))
peso = float(input("DIGITE SEU PESO EM KG: "))


#processamento

imc = peso / (altura ** 2)

def peso ():
    if imc < 25:
        print(f"VOCÊ ESTA COM PESO NORMAL, IMC DE: {imc}")
    elif imc >= 25 and imc < 30:
        print(f"VOCÊ ESTA OBESO, COM IMC DE: {imc}")
    elif imc > 30:
        print(f"VOCÊ ESTA COM OBESIDADE MÓRBIDA, COM IMC DE: {imc}")

#saida

peso()