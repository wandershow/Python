'''Crie um programa que tenha varias palavras (não usar acentos)
depois disso voce deve mostrar para cada palvra quais são suas vogais'''

palavra = ('gremio', 'inter', 'amor', 'lanche', 'bauru')
vogal = ''
for c in range(0, len(palavra)):
    for cont in range(0, len(palavra[c])):
        if palavra[c][cont] == 'a' or palavra[c][cont] == 'e' or palavra[c][cont] == 'i' or palavra[c][cont] == 'o' \
                or palavra[c][
            cont] == 'u':
            vogal += palavra[c][cont] + ' '

    print(f'Na palavra {palavra[c].upper()} temos {vogal}')
    vogal = ''

''' Soluçaõ guanabara'''
palavra = ('gremio', 'inter', 'amor', 'lanche', 'bauru')
for p in palavra:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
