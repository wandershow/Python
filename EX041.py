# leia o ano de nascimento de um atleta, e mostre sua categoria, de acordo com sua idade
from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))

if (date.today().year - nascimento) <= 9:
    print('MIRIM')
elif (date.today().year - nascimento) <= 14:
    print('INFANTIL')
elif (date.today().year - nascimento) <= 19:
    print('JUNIOR')
elif (date.today().year - nascimento) <= 20:
    print('SENIOR')
else:
    print('MASTER')