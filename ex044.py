# elabore um programa que calcule o valor a ser pago por um produto, considerando sua condição de pagamento
# Dinheiro ou cheque 10% de desconto
# A vista no cartão 5% de desconto
# em ate 2x no cartão preço normal
# 3x ou mais no cartão 20% de juros

produto = float(input('Digite o valor do produto? '))

pagamento = int(input(' Escolha a forma de pagamento:\n 1- Dinheiro ou cheque a vista\n 2- Debito\n 3- 2x no cartão '
                      'de credito\n 4- 3x no cartão\n '))

if pagamento == 1:
    print('O valor do seu produto com 10% de desconto R${:.2f}'.format(produto * 0.9))
elif pagamento == 2:
    print('O valor do seu produto com 5% de desconto R${:.2f}'.format(produto * 0.95))
elif pagamento == 3:
    print('O valor do seu produto em 2x pelo preço a vista R${:.2f}'.format(produto))
elif pagamento == 4:
    print('O valor do seu produto com 20% de acrescimo R${:.2f}'.format(produto * 1.2))
