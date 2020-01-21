#entrada
seg = int(input())


#processamento

def main():    
    hora = seg // 3600
    rest = seg % 3600
    minu = rest // 60
    segundos = rest % 60
    print("{}:{}:{}".format(hora,minu,segundos) )

	
#saida
	
main ()