#entrada e processamento

def idade():
    dias = int(input())
    anos = dias // 365
    resto_ano = dias % 365
    mes = resto_ano // 30
    dia = resto_ano % 30
    print(anos,"ano (s)")
    print(mes,"mes (es)")
    print(dia,"dia (s)")

#processamento

idade()