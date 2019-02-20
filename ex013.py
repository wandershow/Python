# leia o salario de um funcionario, e mostre com 15% de aumento

s = float(input('Digite o valor do salario: '))
print(' Esse e o seu salario R${:.2f} \n Esse e o seu novo salario com 15% de aumento R${:.2f}'.format(s, s *1.15))