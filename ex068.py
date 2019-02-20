'''Faça um programa que jogue par ou impar com o computador. o jogo sera interrompido quando o jogador perder.
mostrando o total de vitorias consecutivas que ele conquistou no final do jogo'''

from random import choice
comp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e = choice(comp)
count = 0
while True:
    print('+'*50)
    print('         VAMOS JOGAR PAR OU IMPAR?')
    print('+'*50)
    v = int(input('Diga um valor: '))
    s = str(input('Par ou Impar? [P/I]')).strip().upper()
    r = v + e
    print(f'Voce jogou {v} e o computador jogou {e}')
    if (s == 'P' and r%2 == 0) or (s == 'I' and r%2 == 1):
        print('Voce ganhou')
        count += 1
    else:
        break
print(f'Voce perdeu!!! GAME OVER...')
print(f'Voce venceu {count} vezes consecutivas!')
