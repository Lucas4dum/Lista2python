# 1) Escreva um programa que leia a idade de 10 pessoas e armazene-as em uma lista.
# Calcule e mostre:
# a) a menor idade
# b) a média das idades
# c) a quantidade de pessoas que tem idade entre 20 e 30 anos (inclusive)
# d) a quantidade de pessoas com idade maior que a média
import random
pessoas = ['Lucas', 'Otavio', 'Jaine', 'Daniel', 'Vinicius', 'Samuel', 'Lulemor', 'Jose', 'Turri', 'Pedrinho']
idade = []
qtdentre=total=qtd=maiorqtd=0
for i in range(10):
    idade.append(i)    
    idade[i] = random.randint(18,35)
    print("Pessoa:",pessoas[i],"tem",idade[i],"anos de idade\n")    
    if 19 < idade[i] and idade[i] < 31:     
        qtdentre+=1           
    total+=idade[i]
    qtd+=1    
media=round(total/qtd)
for j in range(10):
    if media < idade[j]:        
        maiorqtd+=1
print("Quantidade de pessoas que tem idade entre 20 e 30 anos :",qtdentre,"\n")
print("Média das idades:",media,"\n")
print("Quantidade de pessoas com idade maior que a média:",maiorqtd,"\n")
print("Menor idade: ",min(idade))