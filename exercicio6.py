# 6) Faça um programa que percorra duas listas e gere uma terceira lista sem os elementos 
# repetidos. Mostra na tela as 3 listas.
import random 
listaa=[]
listab=[]
listac=[]
listad=[]
for i in range(10): 
    listaa.append(random.randint(1,10))    
    listab.append(random.randint(1,10))    
    if 9 == i:
        print(listaa,"A")
        print(listab,"B")
listac=list(set(listaa).intersection(listab))
for i in range(10):
    rep1=0
    rep2=0
    for j in range(len(listac)):        
        if listac[j] != listaa[i]:
            rep1+=1
        if listac[j] != listab[i]:
            rep2+=1
    if rep1 == len(listac):
        listad.append(listaa[i])
    if rep2 == len(listac):
        listad.append(listab[i])
print(listac,"C repetidos")
print(listad,"D não repetidos")


