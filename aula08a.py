import math

n = int(input('Digite um numero: '))
raiz = math.sqrt(n)
print('A raiz de {} e igual a {}'.format(n, raiz))
print('A raiz de {} arredondada para baixo é igual a {}'.format(n, math.floor(raiz)))
print('A raiz de {} arredondada para cima é igual a {}'.format(n, math.ceil(raiz)))
