'''Faça um programa que leia o nome e peso de varias pessoas, guardando tudo em uma lista. no final, mostre:
quantas pessoas foram cadastradas
uma listagem com as pessoas mais pesadas
uma listagem com as pessoas mais leves'''

dado = list()
lista = list()
maisleve = maispesado = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    lista.append(dado[:])
    if len(lista) == 1:
        maispesado = dado[1]
        maisleve = dado[1]
    if dado[1] > maispesado:
        maispesado = dado[1]
    if dado[1] < maisleve:
        maisleve = dado[1]
    r = str(input('VOCÊ QUER CONTINUAR? [S/N]'))
    if r in 'Nn':
        break
    dado.clear()

print('='*30)
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi de {maispesado}Kg. Peso de ', end='')
for p in lista:
    if p[1] == maispesado:
        print(p[0], end=' ')
print(f'\nO menor peso foi de {maisleve}Kg. Peso de ', end='')
for p in lista:
    if p[1] == maisleve:
        print(p[0], end=' ')
