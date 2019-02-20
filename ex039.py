# faça um programa que leia o ano de nascimento de um jovem e de acordo com a sua idade
# se ele ainda vai se alistar, e quanto tempo falta
# se ele tem que se alistar
# se ja passou quanto tempo faz
from datetime import date

nascimento = int(input('Digite seu ano de nascimento: '))

if (date.today().year - nascimento) == 18 :
    print('Você tem que se alistar esse ano!!')
elif (date.today().year - nascimento) < 18 :
    print('Voce precisa se alistar no ano de {}'.format((18 - (date.today().year - nascimento)) + date.today().year))
else:
    print('Voce deveria ter se alistado no ano de {}'.format((date.today().year - ((date.today().year - nascimento)-18))))