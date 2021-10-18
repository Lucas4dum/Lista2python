# 7) Escreva um programa que gere uma lista que é
#  resultado do produto de duas listas L1 e 
# L2. Mostre na tela as 3 listas.
import random 
l1=[]
l2=[]
l3=[]
valor=0
for i in range(5):
    l1.append(random.randint(1,10))
    l2.append(random.randint(1,10))
    valor=l1[i]*l2[i]
    l3.append(valor)
print(l1)
print(l2)
print(l3)