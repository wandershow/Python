# Escreva um programa que faça o computador pensar em um numero entre 0 e 5 e peça para o usuario tentar descobrir,
# qual foi o numero escolhido pelo computador.
# O programa devera escrever na tela se o usuario venceu ou perdeu

from random import choice
from time import sleep
n = [0, 1, 2, 3, 4, 5]
escolhido = choice(n)
print('=' * 150)
print(' Vou pensar em um numero de 0 a 5!!!')
print('=' * 150)
palpite = int(input('Digite o seu palpite entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3)                                                    # serve para fazer o computador demorar um pouquinho para
                                                            # dar a resposta, eu defino em segundos...
if palpite == escolhido:
    print('Voce acertou!!!')
else:
    print('Voce errou!!!')
    print('o numero escolhido pelo computador foi {}'.format(escolhido))

