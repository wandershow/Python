'''Crie um programa que leia o nome e o preço de varios produtos.O programa devera perguntar se o usuario vai
continuar. no final mostre
Qual é o total gasto na compra
quantos produtos custam mais de R$1000
Qual é o nome do produto mais barato'''
total = 0
caro = 0
produto = ''
barato = 0
c = 1

while True:
    r = ''
    nome = str(input('nome do produto: ')).strip().lower()
    valor = float(input('Valor do produto R$'))
    total += valor
    if valor > 1000:
        caro += 1
    if c == 1 or barato > valor:
        barato = valor
        produto = nome
        c += 1
   #while r not in 'SN': #faz a mesma coisa que o while de baixo
    while r != 'S' and r != 'N':
        r = str(input('Quer continuar? [S/N]')).strip().upper()
    if r == 'N':
        break
print(f'O total de gastos é R${total:.2f}')
print(f'{caro} produtos custam mais de R$1000.00 reais')
print(f'O produto mais barato é {produto} seu valor é R${barato:.2f}')