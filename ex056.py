# Desenvolva um program que leia o nome, idade e sexo de 4 pessoas. no final mostre:
# A media de idade do grupo
# Qual é o nome do homen mais velho
# Quantas mulheres tem menos de 21 anos

nome = [0]*4
idade = [0]*4
sexo = [0]*4
media = 0
velho = 0
mulheres = 0
for c in range(0, 4):
    nome[c] = str(input('Digite o nome: '))
    idade[c] = int(input('Digite a idade:'))
    sexo[c] = str(input('Digite o sexo: '))
    media = media + idade[c]
    if 'm' in sexo[c] and idade[c] > velho:
        velho = idade[c]
    if 'f' in sexo[c] and idade[c] < 21:
        mulheres = mulheres + 1
media = media / 4

print('A media de idade do grupo é de: {} anos'.format(media))
print('O homen mais velho tem {} anos'.format(velho))
print('Tem {} mulheres menores de 21 anos no grupo'.format(mulheres))