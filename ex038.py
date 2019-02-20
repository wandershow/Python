# Escreva um programa que leia dois numero e diga qual e o maior ou se são iguais

n1 = int(input('digite o primeiro numero:'))
n2 = int(input('digite o segundo numero:'))

if n1 > n2:
    print('O primeiro valor é maior.')
elif n1 < n2:
    print('O segundo valor é maior')
else:
    print(n1,'e',n2, 'São iguais')