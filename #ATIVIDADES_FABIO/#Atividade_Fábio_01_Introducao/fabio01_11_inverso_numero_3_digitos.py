#-*-coding:utf8;-*-
#qpy:3
#qpy:console


#entrada 
numero = int(input("Informe um número de 3 dígitos: ")) 

#processamento 
und = numero % 10 
cen = numero // 100 
numero = numero 
dez = numero % 100 
dez = dez // 10 
und = und * 100
dez = dez *10
cen = cen *1
inverso = und+cen+dez

#saida
print("O Inverso é: ",inverso,)

