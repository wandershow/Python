# Desenvolva um programa que leia o primeiro termo e a razao de Progressão Aritmetica, no final mostre os 10 primeiros
# termos dessa progressão.

n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão aritmetica: '))
for c in range(0, 10):
    print(n, end='-> ')
    n += r

