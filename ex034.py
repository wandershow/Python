#escreva um programa que leia o salrio de um funcionario e mostre o seu aumento,se for menor que 1250 o aumento e de
# 15% se for maior de 10%

s = float(input('Qual o valor do salario? '))
if s <= 1250:
    print('R${:.2f} foi aumentado em 15% e ficou sendo R${:.2f}'.format(s, s *1.15))
else:
    print('R${:.2f} foi aumentado em 10% e ficou sendo R${:.2f}'.format(s, s * 1.10))
