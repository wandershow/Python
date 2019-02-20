# crie um programa que leia duas notas de um aluno e calcule sua media.
# mostrando uma mensagem no final de acordo com a media atingida

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) /2

if media < 5.0:
    print('Reprovado')
elif media >= 5.0 and media <= 6.9:
    print('Recuperação')
else:
    print('APROVADO')