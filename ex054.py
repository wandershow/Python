# crie um programa que leia o ano de nascimento de sete pessoas. no final mostre quantas delas ainda não atingiram a
# maioridade e quantas ja sao maiores
from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    n = int(input('Digite o ano de nascimento: '))
    if (ano - n) >= 18:
        maior = maior +1
    else:
        menor = menor +1
print('{} São maiores!'.format(maior))
print('{} São menores!'.format(menor))