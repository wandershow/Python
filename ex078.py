'''Faça um programa que leia 5 numeros do teclado e guarde os em uma lista
no final mostre qual foi o maior e o menor valor e suas respectivas posições na lista'''

valores = list()
for v in range(0, 5):
    valores.append(int(input('Digite o valor: ')))
print(f'Os valores que você digitou são {valores}')
print(f'O maior valor é: {max(valores)} e esta nas posições ', end='')
for p, v in enumerate(valores):
    if max(valores) == v:
        print(p, end='... ')
print(f'\nO menor valor é: {min(valores)} e esta nas posições ', end='')
for p, v in enumerate(valores):
    if min(valores) == v:
        print(p, end='... ')

''' Aqui mostra o menor e o menor e a sua posição onde cada aparece pela primeira vez '''
print(f'\n\n{valores}')
print(f'O maior valor é: {max(valores)} e esta na posição {valores.index(max(valores))}')
print(f'O menor valor é: {min(valores)} e esta na posição {valores.index(min(valores))}')

