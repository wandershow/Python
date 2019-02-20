# Faça um programa que leia um numero inteiro e diga se ele é ou nao primo

n = int(input('Digite um numero: '))
a = 0

for c in range(2, n+1):
    if n % c == 0:
        a += 1
if a > 1:
    print('{} Não é primo'.format(n))
else:
    print('{} É primo'.format(n))






