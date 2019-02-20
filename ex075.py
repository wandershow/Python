'''Desenvolva um programa que leia 4 valores do teclado e guarde os em uma tupla e mostre
quantas vezes apareceu o valor 9
Em que posição foi digitado o valor 3 pela primeira vez
Quais foram os numeros pares
'''
cont = 0
pos = 0
par = 0
numero = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')), int(input('Digite mais um numero: ')),
     int(input('Digite o ultimo numero: ')))
for c in range(0, len(numero)):
    if numero[c] == 9:
        cont += 1
    if numero[c] == 3 and pos == 0:
        pos = c + 1
    if numero[c] % 2 == 0:
        par += 1
print(f'Voce digitou os numeros {numero}')
if cont == 0:
    print('o valor 9 nao apareceu nenhuma vez')
else:
    print(f'o valor 9 apareceu {cont} vezes')
if pos > 0:
    print(f'o valor 3 apareceu na {pos}º posição')
else:
    print('o valor 3 não apareceu nenhuma vez')
if par > 0:
    print(f'Tem {par} numeros par')
else:
    print('Não tem nenhum numero par...')

'''Soluçao guanabara'''

numero = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')), int(input('Digite mais um numero: ')),
     int(input('Digite o ultimo numero: ')))
print(f'Voce digitou os numeros {numero}')
print(f'o valor 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'o valor 3 apareceu na {numero.index(3)+1}º posição')
else:
    print('o valor 3 foi digitado nenhuma vez')
print('Os valores pares digitados foram ', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')