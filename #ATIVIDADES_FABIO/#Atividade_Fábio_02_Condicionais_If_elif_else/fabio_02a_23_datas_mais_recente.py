#entrada

dia_um = int(input("DIGITE O DIA DA PRIMEIRA DATA: "))
mes_um = int(input("DIGITE O MÊS DA PRIMEIRA DATA: "))
ano_um = int(input("DIGITE O ANO DA PRIMEIRA DATA: "))

dia_dois = int(input("DIGITE O DIA DA SEGUNDA DATA: "))
mes_dois = int(input("DIGITE O MÊS DA SEGUNDA DATA: "))
ano_dois = int(input("DIGITE O ANO DA SEGUNDA DATA: "))


#processamento

def principal ():
    if dia_um or dia_dois or mes_um or mes_dois or ano_um or ano_dois == 0:
        mes_valido()
    else:
        print("INFORME UMA DATA VALIDA")

def mes_valido ():
    if mes_um and mes_dois > 0 and mes_um and mes_dois < 12:
        dia_valido()
    else:
        print("INFORME UM MÊS VALIDO")
        
def dia_valido ():
    if dia_um and dia_dois > 0 and dia_um and dia_dois < 31:
        data_recente()
    else:
        print("INFORME UM DIA VALIDO")


def data_recente ():
    if ano_um > ano_dois:
       print("A PRIMEIRA DATA É A MAIS RECENTE")
    elif ano_dois > ano_um:
        print("A SEGUNDA DATA É A MAIS RECENTE")
    elif ano_um == ano_dois:
        if mes_um > mes_dois:
            print("A PRIMEIRA DATA É A MAIS RECENTE")
        elif mes_dois > mes_um:
            print("A SEGUNDA DATA É A MAIS RECENTE")
        elif mes_um == mes_dois:
            if dia_um > dia_dois:
                print("A PRIMEIRA DATA É A MAIS RECENTE")
            elif dia_dois > dia_um:
                print("A SEGUNDA DATA É A MAIS RECENTE")   


#saida

principal()