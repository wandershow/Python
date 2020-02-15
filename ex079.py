'''Crie um programa onde o usuario digite varios valores numericos e cadastre-os em uma lista.
caso o numero ja exista la dentro ele não sera adicionado, no final serão exibidos todos os valores unicos digitados
em ordem crescente.'''

valores = list()

while True:
    n = int(input('Digite um valor: '))
    if n in valores:
        print('Valor Duplicado! Não vou adicionar!')
    else:
        valores.append(n)
        print(f'Valor {n} adicionado com sucesso')
    pergunta = str(input('Você quer Continuar? [S/N] ')).upper()
    while pergunta != 'S' and pergunta != 'N':
        pergunta = str(input('DIGITE UM VALOR VALIDO!! Você quer Continuar? [S/N] ')).upper()
    if pergunta in 'Nn':
        break
print(f'Estes são os valores digitados {valores}')
valores.sort()  # aqui faz a ordenação
print(f'Estes são os valores digitados ordenados na ordem crescente {valores}')