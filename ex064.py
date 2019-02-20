'''Crie um programa que leia varios numeros inteiros pelo teclado. o programa só para quando o usuario digitar 999,
que é a condição de parada do programa, no final mostre quantos numeros foram digitados e qual foi a soma entre eles
desconsiderando o flag'''
n = 0
count = 0
soma = 0
while n != 999:
    soma += n
    n = int(input('Digite o numero: ou 999 para sair '))
    count += 1
print('A soma dos valores é {}'.format(soma))
print('A quantidade de valores lida é {}'.format(count-1))