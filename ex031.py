# Pergunte a distancia de uma viagem em km, e calcule o preço da passagem cobrando R$0.50 por km para viagens de ate
# 200 km e R$0.45 para viagens mais longas.

d = int(input('Qual a distancia da viagem? '))
if d <200:
    v = d * 0.50
    print('o valor da passagem é de R${:.2f}'.format(v))
else:
    v = d * 0.45
    print('o valor da passagem é de R${:.2f}'.format(v))