# 2) Faça um programa que preencha uma lista com 10 cores diferentes. Depois permita fazer 
# uma pesquisa se uma determinada cor existe armazenada na lista, se existir deve ser 
# impresso na tela a cor e em qual posição (índice) esta cor está armazenada. A pesquisa 
# deve ser feita até que seja digitado FIM na cor a ser pesquisada na lista.
import random
posicao=0
cores = ['Azul', 'Preto', 'Amarelo', 'Branco', 'Roxo', 'Vermelho','Laranja', 'Verde', 'Rosa', 'Cinza']
print(cores)
texto =str(input("Busque uma dessas cores: "))
while texto.upper() != 'FIM': 
    achou=0
    for i in range(10):
        if cores[i].upper() == texto.upper():
            achou=1
            posicao=i
    if achou == 1:
        print("Cor ",cores[posicao],"existe na lista e está na posição: ",posicao)
    else:
        print("Não existe na lista")
    texto =str(input("Busque uma dessas cores: "))

