'''Aprimore o desafio anterior, mostrando no final:
A soma de todos os valores pares digitados
A soma dos valores da terceira coluna.
o maior valor da segunda linha'''

matriz =[[], [], []]
p = 0
c = 0
par = coluna = linha = 0
while True:
    n = int(input(f'Digite um numero: para posição [{p}, {c}]: '))
    if n % 2 == 0:
        par += n
    matriz[p].append(n)
    if c == 2:
        coluna += n
    c += 1
    if p == 2 and c == 3:
        break
    if c == 3:
        c = 0
        p += 1
print('-='*30)
for n in matriz:
    print(f'[ {n[0]:^5} ][ {n[1]:^5} ][ {n[2]:^5} ]')
print('-='*30)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da 3º coluna é {coluna}')
print(f'O maior valor da 2º linha é {max(matriz[1])}')