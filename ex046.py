#Faça na tela um programa que mostre na tela uma contagem regressiva de 10 ate 0 com uma pausa de 1 segundo entre
# eles para o estouro dos fogos!

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BOOOOOOOM!!!')

