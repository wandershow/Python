# Faça um programa que leia o sexo de uma pessoa mas só aceite os valores 'M' ou 'F', caso esteja errado peça a
# digitação novamente ate ter um valor correto

s = str(input('Digite o seu sexo: [M/F] ')).strip().upper()
while s != 'M' and s != 'F':
    s = str(input('Voce digitou errado, digite [M/F] ')).strip().upper()
print('Seu sexo é {}'.format(s))

''' outra maneira de usar o while com string 

s = str(input('Digite o seu sexo: [M/F] ')).strip().upper()
while s not in 'MmFf':
    s = str(input('Voce digitou errado, digite [M/F] ')).strip().upper()
print('Seu sexo é {}'.format(s))

'''