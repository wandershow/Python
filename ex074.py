''' crie um programa que crie 5 numeros aleatorios e coloque em uma tupla
depois disso mostre a listagem dos numeros criados o menor e o maior numero'''

from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = 0
menor = 0
for c in range(0, 5):
    if c == 0:
        maior = numeros[c]
        menor = numeros[c]
    if numeros[c] > maior:
        maior = numeros[c]
    if numeros[c] < menor:
        menor = numeros[c]


print(f'Estes sao os valores sorteados {numeros}')
print(f'Este é o maior valor sorteado {maior}')
print(f'Este é o menor valor sorteado {menor}')

''' Resolução guanabara'''
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('\nOs valores sorteados foram: ', end='')
for n in num:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')