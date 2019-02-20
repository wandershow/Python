'''Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada o programa devera perguntar
se o usuario quer ou nao continuar, no final mostre:
Quantas pessoas tem mais de 18 anos
Quantos homens fora cadastrados
Quantas mulheres tem menos de 20 anos'''


people = 0
man = woman = 0
p = ''
while True:
    idade = 0
    sexo = ''

    while idade < 1:
        idade = int(input('Digite a idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite o sexo: [M/F]')).strip().upper()
    if idade > 18:
        people += 1
    if sexo == 'M':
        man += 1
    if sexo == 'F' and idade < 20:
        woman += 1
    while p != 'S' and p != 'N':
        p = str(input('VOCE QUER CONTINUAR? [S/N]')).strip().upper()
    if p == 'N':
        break

print(f'Tem {people} pessoas maiores de 18 anos')
print(f'Tem {man} homens cadastrados')
print(f'Tem {woman} mulheres cadastradas com menos de 20 anos')