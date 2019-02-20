''' Crie um programa que leia varios numeros inteiros pelo teclado. o programa só vai parar quando o usuario digitar
o valor 999 que é a condição de parada. No final mostre quantos numeros foram digitados e qual foi a soma entre eles(
Desconsiderando a flag)'''
c = 0
soma = 0
while True:
    n = int(input('Digite o numero: ou [999] para parar'))
    if n == 999:
        break
    c += 1
    soma += n
print(f'Foram digitados {c} numeros.')
print(f'A soma entre eles é {soma}')