'''Crie um programa que leia varios numeros e colocar em uma lista, depois disto mostre:
quantos numeros foram digitados
a lista de valores ordenada de forma decrescente
se o valor 5 foi digitado e esta ou não na lista
'''

valores = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    pergunta = str(input('Voce deseja continuar ? [S/N]')).upper()
    while pergunta != 'S' and pergunta != 'N':
        pergunta = str(input('VALOR INVALIDO! Voce deseja continuar ? [S/N]'))
    if pergunta in 'Nn':
        break
print(valores)
print(f'Foram digitados {len(valores)} valores')
print(f'mostrando em ordem decrescente {sorted(valores, reverse=True)}')
if 5 in valores:
    print(f'O numero 5 foi digitado na posição numero {valores.index(5)}')
else:
    print('O numero 5 não foi digitado!!')
