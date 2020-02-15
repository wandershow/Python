'''Crie um programa onde o usuario digite uma expressão qualquer que use parenteses
seu aplicativo devera analisar se a expressão passada esta com os parentes abertos e fechados na ordem correta'''

valor = str(input('Digite a expressão: '))
if valor.count('(') == valor.count(')'):
    print('Sua expressão esta correta')
else:
    print('Expressão invalida!')