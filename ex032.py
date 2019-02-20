# Faça um programa que leia um ano e diga se ele e bissexto
# Chama-se ano bissexto o ano ao qual é acrescentado um dia extra,
# ficando ele com 366 dias, um dia a mais do que os anos normais de 365 dias,
# ocorrendo a cada quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400)
from datetime import date
ano = int(input('Digite o ano, ou digite 0 se quiser saber se o ano atual é bissexto: '))
if ano == 0:
    ano = date.today().year       # aqui pega o ano atual!!!
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é bissexto'.format(ano))
else:
    print('{} Nao é bissexto'.format(ano))