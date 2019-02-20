'''Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. o
programa sera interrompido quando o numero solicitado for negativo'''

while True:
    c = 0
    print('-' *50)
    n = int(input('Digite o numero para saber sua tabuada: '))
    print('-' *50)
    if n < 0:
        break
    while c <= 10:
        print(f'{n} x {c} = {n*c}')
        c += 1

