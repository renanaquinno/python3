#entrada

salario = float(input())


#processamento
 
def imposto_de_renda (salario):
     oito = 0
     dezoito = 0
     vinte_oito = 0
     if salario < 2000:
           pass

     elif salario > 2000:
          oito = salario - 2000
          if oito > 1000:
               dezoito = oito - 1000
               oito = 1000            
               if dezoito > 1500:
                    vinte_oito = dezoito - 1500
                    dezoito = 1500
                    oito = 1000
     oito = (oito * 8) / 100
     dezoito = (dezoito * 18) / 100
     vinte_oito = (vinte_oito * 28) / 100
     total = (oito + dezoito + vinte_oito)
     
     if salario <= 2000:
          print("Isento")
     else:
          print("R$ {:.2f}".format(total))


#saida

imposto_de_renda(salario)