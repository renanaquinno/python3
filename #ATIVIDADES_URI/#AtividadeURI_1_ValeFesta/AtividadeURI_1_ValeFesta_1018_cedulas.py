#entrada e processamento

def cedulas ():
    dinheiro = int(input())
    sem = dinheiro // 100
    resto_sem = dinheiro % 100
    ciquenta = resto_sem // 50
    resto_ciquenta = resto_sem % 50
    vinte =  resto_ciquenta // 20
    resto_vinte = resto_ciquenta % 20
    dez = resto_vinte // 10
    resto_dez = resto_vinte % 10
    cinco = resto_dez // 5
    resto_cinco = resto_dez % 5
    dois = resto_cinco // 2
    um = resto_cinco % 2
   
    print(dinheiro)
    print(sem,"nota(s) de R$ 100,00")
    print(ciquenta,"nota(s) de R$ 50,00")
    print(vinte,"nota(s) de R$ 20,00")
    print(dez,"nota(s) de R$ 10,00")
    print(cinco,"nota(s) de R$ 5,00")
    print(dois,"nota(s) de R$ 2,00")
    print(um,"nota(s) de R$ 1,00")


#saida

cedulas()