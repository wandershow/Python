''' Crie um programa que crie uma matriz de dimensão 3x3 com valores lidos pelo teclado
no final mostre a matriz na tela com a formatação correta'''

matriz =[[], [], []]
p = 0
c = 0
while True:
    n = int(input(f'Digite um numero: para posição [{p}, {c}]: '))
    matriz[p].append(n)
    c += 1
    if p == 2 and c == 3:
        break
    if c == 3:
        c = 0
        p += 1
for n in matriz:
    print(f'[ {n[0]:^5} ][ {n[1]:^5} ][ {n[2]:^5} ]')

'''RESOLUÇÃO GUANABARA
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] =int(input(f'Digite um numero: para posição [{p}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')   # :^5  *Serve para alinhar ao centro em 5 espaços
    print()
'''