#entrada

t=input().split()
hi=int(t[0])
mi=int(t[1])
hf=int(t[2])
mf=int(t[3])


#processamento

if hi==hf:
     if mi==mf:
          ht=24
          mt=0
     elif mi<mf:
          ht=0
          mt=mf-mi
     else:
          ht=24-1
          mt=(mf+60)-mi
if hi>hf:
     if mi==mf:
          ht=(24-hi)+hf
          mt=0
     elif mi>mf:
          mt=(60+mf)-mi
          ht=(23-hi)+hf
     else:
          mt=mf-mi
          ht=(24-hi)+hf
          
if hi<hf:
     if mi==mf:
          ht=hf-hi
          mt=0
     elif mi>mf:
          mt=(mf+60)-mi
          ht=(hf-hi)-1
     else:
          mt=mf-mi
          ht=hf-hi
 
 
#saida
 
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(ht,mt))