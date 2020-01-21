#entrada e processamento

def populacao ():
    habitantes_a = 200000
    habitantes_b = 800000
    anos = 0
    while habitantes_a < habitantes_b:
       anos += 1
       habitantes_a += (habitantes_a * 0.035)
       habitantes_b += (habitantes_b * 0.0135)    
    
    print(f"Vai demorar {anos} anos")
         
    
#saida

populacao()