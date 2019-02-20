'''Refaça o DESAFIO 051.lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
utilizando o while'''

n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão aritmetica: '))
c = 0
while c < 10:
    print(n, end='-> ')
    n += r
    c += 1