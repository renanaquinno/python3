def main():
    nota_um = float(input())
    
    nota_dois = float(input())

    nota_um_peso = nota_um * 3.5
    
    nota_dois_peso = nota_dois * 7.5
    	
    media = nota_um_peso + nota_dois_peso

    media_total = media / 11
    
    print("MEDIA = {:.6}".format(media_total))   

main ()