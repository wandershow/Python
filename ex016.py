#leia um numero real qualquer e mostre a sua parte inteira
from math import trunc, floor
n = float(input('Digite um numero: '))
print('a porçao inteira é: {}'.format(floor(n)))

print('a porção inteira é: {}'.format(trunc(n)))

print('a porção inteira é: {}'.format(int(n)))