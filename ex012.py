# leia o preço de um produto e mostre seu novo preço com 5% de desconto

p = float(input('Qual o preço? '))

print('o valor do seu produto passou de R${:.2f}, para R${:.2f}, com 5% de desconto!!!'.format(p, p * 0.95))