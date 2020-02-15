'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios.
guarde esses resultados em um dicionario. No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o
maior numero do dado.'''

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = list()
print('Valores Sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #aqui organiza em ordem decrescente pela posição 1
# key=itemgetter(1) numero do dado **se fosse 0 pegaria o jogador, reverse true e para colocar em ordem decrecente

print('-='*30)
print(' RANKING DOS JOGADORES')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]} ')
    sleep(1)







