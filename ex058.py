# Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um numero entre 0 e 10. só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer

from random import choice
from time import sleep
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolhido = choice(n)
contador = 1
print('=' * 150)
print(' Vou pensar em um numero de 0 a 10!!!')
print('=' * 150)
palpite = int(input('Digite o seu palpite entre 0 e 10: '))
print('PROCESSANDO...')
sleep(3)                                                    # serve para fazer o computador demorar um pouquinho para
                                                            # dar a resposta, eu defino em segundos...
while palpite != escolhido:
    print('Voce errou tente de novo!!')
    print('')
    palpite = int(input('Digite o seu palpite entre 0 e 10: '))
    print('PROCESSANDO...')
    sleep(0.5)
    contador += 1

print('VOCÊ GANHOU!!!, mas precisou de {} tentativas'.format(contador))