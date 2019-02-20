'''Refaça o DESAFIO 061.lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
utilizando o while, e depois pergunte para o usuario se ele quer mostrar mais alguns termos. o programa encerra
quando ele disser que quer 0 termos'''

n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão aritmetica: '))
count = 0
c = 0
cont = 10
while c < cont:
    print(n, end='-> ')
    n += r
    c += 1
    if c == cont:
        p = int(input('Quantos termos mais voce gostaria de mostrar? '))
        if p > 0:
            cont = cont + p
    count += 1
print('Progressão finalizada com {} termos mostrados'.format(count))