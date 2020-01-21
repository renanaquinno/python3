#entrada

x = 1
y = 0


# processamento

def ordem (x, y):
    while x != y:
        valores = input().split()
        x = int(valores[0])
        y = int(valores[1])
        if y > x:
            print("Crescente")
        elif x > y:
            print("Decrescente")
                
    
#saida

ordem(x, y)