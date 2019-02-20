#Refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher so que agora utilizando for

n = int(input('digite um numero inteiro: '))

for c in range(1, 11):
    print('{:2} x {} = {}'.format(c, n, c*n))