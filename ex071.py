'''Crie um programa que simule o funcionamento de um caixa eletronico. no inicio pergunte ao usuario quanto ele quer
sacar (inteiro) e o programa vai informar quantas cedulas de cada valor serão entregues.
considere que o caixa possui cedulas de R$50, R$20, R$10, e R$1'''

valor = int(input('Quanto você quer sacar? '))
'''cinquenta = int(valor/ 50)
vinte = int(valor%cinquenta)//20
dez = int(valor%vinte)//10
print(cinquenta, vinte, dez)'''
c = 0
v = 0
d = 0
u = 0
while True:
    while valor >= 50:
        valor -= 50
        c += 1
    if c > 0:
        print(f'{c} notas de R$50.00')
    while valor >= 20:
        valor -=20
        v += 1
    if v > 0:
        print(f'{v} notas de R$20.00')
    while valor >= 10:
        valor -= 10
        d +=1
    if d > 0:
        print(f'{d} notas de R$10.00')
    while valor >= 1:
        valor -= 1
        u += 1
    if u > 0:
        print(f'{u} notas de R$1.00')
    if valor == 0:
        break

