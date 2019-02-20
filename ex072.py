''' Crie um programa que leia um numero entre zero e 20 do teclado e escreva seu numero por extenso'''

n = int(input('Digite um numero entre 0 e 20: '))

while 0 < n > 20:
    n = int(input('NUMERO INVALIDO!!!, Digite um numero entre 0 e 20: '))

numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print(f'você digitou o numero {numero[n]}')

''' Resolução guanabara

numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while true:
    n = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= n >= 0:
        break
    print('Tente novamente. ', end='')
print(f'você digitou o numero {numero[n]}')'''