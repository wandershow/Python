'''Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma
sequencia de fibonatti'''

n = int(input('Digite o numero para saber a sequencia de fibonacci: '))
r = 1
a = 0
c = 0
s = [0]*n
while c < n:
    s[c] = a
    print(s[c], end='-> ')
    a = r + a
    r = s[c]
    c += 1

