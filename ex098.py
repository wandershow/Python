''' Faça um programa que tenha uma função chamada contador().
que receba tres parametros:inicio, fim e passo e realize a contagem.
Seu programa tem que realizar tres contagens atraves da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 30)

    if inicio > fim:
        if passo == 0:
            passo = 1
        if passo > 0:
            passo = passo * (-1)
        print(f'Contagem de {inicio} até {fim} de {passo * (-1)} em {passo * (-1)} ')
        fim -= 1
    else:
        if passo < 0 :
            passo *= -1
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo} ')
        fim += 1

    for c in range(inicio, fim, passo):
        print(f'{c}', end=' ', flush=True)
        sleep(0.5)
    print('fim')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)

