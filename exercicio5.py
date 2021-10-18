# 5) Faça um programa que preencha uma lista com os nomes de 5 produtos, e outra lista com 
# o valor dos produtos. Calcule e mostre:
# a. a quantidade de produtos que o valor é abaixo de 10 reais;
# b. a média dos valores dos produtos;
# c. a quantidade de produtos que valor acima da média;
# d. a maior valor e o nome do produto;
# e. faça uma listagem que imprima na tela (Nome Vlr do produto)
import random 
abaixo=maiorvalor=posmaior=valortotal=acima=0
valor = []
produto = ["bolo","baguete","manteiga","achocolatado","café"]
for i in range(5):
    valor.append(random.randint(6,13))
    if i == 0:
        maiorvalor = valor[i]
    if valor[i] < 10:
        abaixo+=1    
    valortotal+=valor[i]
    if maiorvalor < valor[i]:
        maiorvalor = valor[i]
        posmaior = i
media = valortotal/5
for j in range(5):
    if media < valor[j]:
        acima+=1
    print("Nome do produto",produto[j],"valor",valor[j])
    print("")
print("a quantidade de produtos que o valor é abaixo de 10 reais:",abaixo)
print("")
print("a média dos valores dos produtos",media)
print("")
print("a quantidade de produtos que valor acima da média",acima)
print("")
print("a maior valor",valor[posmaior],"e o nome do produto",produto[posmaior])

    