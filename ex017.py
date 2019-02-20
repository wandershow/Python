# faça um programa que leia o cateto oposto e o adjacente de um triangulo retangulo e calcule e mostre a hipotenusa
from math import hypot
c1 = float(input('digite o cateto oposto '))
c2 = float(input('digite o cateto adjacente '))
h = ((c1**2) + (c2**2)) **(1/2)
print('o valor da hipotenusa é {:.2f}'.format(h))

hi = hypot(c1, c2)
print('o valor da hipotenusa é {:.2f}'.format(hi))