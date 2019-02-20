# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salario ou então o financiamneto sera
# negado.

valor_da_casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salario? '))
meses = int(input('Em quantos anos você quer pagar? ')) * 12

prestacao_mensal = valor_da_casa / meses
poder_aquisitivo = salario * 0.30

if prestacao_mensal > poder_aquisitivo:
    print('\nFinanciamneto negado')
    print(' O valor da casa é de R${:.2f}\n O seu salario é R${:.2f} Você quer pagar em {} meses\n O valor maximo que '
          'você '
          'consegue pagar por mes é de R${:.2f}'.format(valor_da_casa, salario, meses, poder_aquisitivo))
else:
    print('Parabens seu financiamento foi aprovado!!!')
    print('O valor da sua prestação é de {:.2f} por mes'.format(prestacao_mensal))
