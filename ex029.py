# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h. mostre uma mensagem dizendo que ele foi multado.
# A multa vais custar R$7.00 por cada k acima do limite.

velocidade = int(input('Digite qual a velocidade do carro: '))

if velocidade > 80:
    m = (velocidade - 80) * 7
    print('Você foi multado!!')
    print('O valor da sua multa é de R${:.2f} Reais'.format(m))
print('Voce esta na velocidade adequada para a via, Tenha um bom dia!!!')

