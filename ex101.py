'''crie um programa que tenha uma função chamada voto() que vai receber o ano de nascimento de uma pessoa,
retornado um valor literal indicando se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.'''

def voto(a=2019):
    idade = 2019 - a
    if idade < 16:
        print(f'com {idade} anos o VOTO E NEGADO')
    elif idade >= 18 and idade < 65:
        print(f'com {idade} anos o VOTO E OBRIGATORIO')
    elif (idade >= 16 and idade < 18) or (idade > 65):
        print(f'com {idade} anos o VOTO E OPCIONAL')

ano = int(input('Qual o ano de seu nascimento?'))
voto(ano)

'''Solução do Guanabara'''
from datetime import date


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos o VOTO E NEGADO'
    elif idade >= 18 and idade < 65:
        return f'com {idade} anos o VOTO E OBRIGATORIO'
    elif (idade >= 16 and idade < 18) or (idade > 65):
        return f'com {idade} anos o VOTO E OPCIONAL'

nasc = int(input("Emque ano vocẽ nasceu? "))
print(voto(nasc))