'''Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta'''

from random import randint
from time import sleep

print('-='*30)
print(' '*18, 'JOGA NA MEGA SENA')
print('-='*30)
qtdjogos = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = list()
lista = list()
for c in range(0, qtdjogos):
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
        if len(lista) == 6:
            break
    jogos.append(lista[:]) # aqui cria uma copia sem ligação "[:]"
    lista.clear()
print(f'SORTEANDO {qtdjogos} JOGOS!!!')
for j in range(0, qtdjogos):
    print(f'jogo {j+1}: {sorted(jogos[j])}', end='\n')
    sleep(1)
print('-=' *5, 'BOA SORTE!', '-='*5)