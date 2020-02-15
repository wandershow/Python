'''Faça um programa que tenha uma função chamada maior(), que receba varios parametros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles e o maior.'''
def maior(*num):
    maior = 0
    print('Analisando os valores passados')
    for c in num:
        if maior < c:
            maior = c
        print(f'{c}', end=' ')
    print('-=' * 30)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()