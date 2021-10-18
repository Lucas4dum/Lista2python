# 8) Escreva um programa que preencha uma lista com os nomes de 5 vendedores, preencha 
# também outra lista com valor total das vendas de cada vendedor. Cada vendedor recebe 
# 10% de comissão sobre as vendas. Faça os seguintes cálculos e mostre os resultados na 
# tela:
# a. Uma listagem com o nome e o valor a receber de cada vendedor (total das 
# vendas * 0.10)
# b. O total (bruto) vendido pelos 5 vendedores
# c. A média do total de vendas (valor bruto vendido por cada vendedor)
# d. A quantidade de vendedores que venderam acima da média das vendas
# e. O maior valor de comissão e o nome do vendedor que recebeu
import random
vendedor=["Lucas","Daniel","Jaine","Otavio","Luquinha"]
comissao=[]
vendas=[]
valor=vendastotal=qtdmaior=maiorcom=posimaior=0
for i in range(5):
    vendas.append(random.randint(5000, 10000))
    valor=vendas[i]*0.1
    comissao.append(valor)
    if i ==0:
        maiorcom=comissao[i]
    if maiorcom < comissao[i]:
        maiorcom = comissao[i]
        posimaior=i
    vendastotal+=vendas[i]
media=vendastotal/5
for j in range(5):
    if media < vendas[j]:
        qtdmaior+=1        
    print("O vendedor",vendedor[j],"o valor a receber",round(comissao[j],2))
    print("A média do total de vendas",media,"\nvalor bruto vendido por ",vendedor[j],"e o total de suas vendas são",vendas[j])
    print("")
print("O total bruto vendido pelos 5 vendedores",vendastotal)
print("")
print("O maior valor de comissão",round(comissao[posimaior],2),"e o nome do vendedor que recebeu",vendedor[posimaior])
print("")
print("A quantidade de vendedores que venderam acima da média das vendas",qtdmaior)

