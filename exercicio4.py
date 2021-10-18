# 4) Faça um programa que preencha duas listas com 10 elementos em cada. Depois percorra 
# essas duas listas e gere uma terceira lista com os números que se repetem nas duas listas. 
# Mostre as três listas na tela.
import random 
listaa=[]
listab=[]
for i in range(10): 
    listaa.append(random.randint(1,10))    
    listab.append(random.randint(1,10))    
    if 9 == i:
        print(listaa,"A")
        print(listab,"B")
listac=(set(listaa).intersection(listab))
print(listac)


