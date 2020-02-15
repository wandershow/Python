'''Faça um programa que tenha uma lista chamada numeros e duas funçoes chamadas sorteia() e somaPar().
A primeira função vai sortear 5 numeros e vai colocalos dentro da lista e a segunda função vai mostrar a soma entre
todos os valores Pares sorteados pela função anterior'''
from random import randint
from time import sleep


numeros = list()
def sorteia():

    print(f'Sorteando 5 valores da lista', end=' ')
    for c in range(0, 5):
        numeros.append(randint(0,10))
        print(f'{numeros[c]}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')



def somaPar():
    soma = 0
    print(f'Somando os valores pares de {numeros}, temos ', end='')
    for c in numeros:
            if c % 2 == 0:
                soma += c
    print(soma)


sorteia()
somaPar()