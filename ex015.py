#: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos kilometros vc percorreu? '))
d = int(input('quantos dias voce ficou com o carro alugado?'))
t = (km * 0.15) + (d * 60)
print('Voce precisa pagar um total de R${:.2f}'.format(t))
