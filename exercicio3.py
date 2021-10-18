# 3) Faça um programa que preencha duas listas, lista A e lista B com 5 números em cada. 
# Gere a lista C, com os números da lista A e lista B. Depois calcule e mostre na tela a 
# quantidade de números perfeitos. Um número é perfeito quando ele é igual a soma dos 
# seus divisores excetuando ele próprio. (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus 
# divisores).
import random
j=0
numeroa=[]
numerob=[]
numeroc=[]
total=valor=0
for i in range(10):
    if 5 > i:
        numeroa.append(random.randint(6,28))  
    if 4 < i:
        j=i-5
        numerob.append(random.randint(490,496))     
numeroc.extend(numeroa)
numeroc.extend(numerob)
print(numeroa,"A")
print(numerob,"B") 
for h in range(10):
    valor=0
    for k in range(1,numeroc[h]):
        if numeroc[h]%k == 0:
            valor+=k
    if valor == numeroc[h] and 0 != numeroc[h]:
        print("O valor:",numeroc[h],"é perfeito")





