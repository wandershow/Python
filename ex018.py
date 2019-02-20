# leia um angulo qualquer e mostre na tela o valor do seno cosseno e tangente desse angulo

from math import sin, cos, tan, radians
ang = float(input('Digite o angulo '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print(' o seno de {}° é {:.2f}°, o cosseno é {:.2f}°, e a tangente é {:.2f}°'.format(ang, seno, cosseno, tangente))