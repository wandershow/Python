# crie um programa que leia o nome de uma cidade e diga se ela começa com a palavra 'santo'

cidade = input('Digite o nome da cidade: ')
inicio = cidade.lower().split()
print('existe a palavra santo no inicio do nome da cidade? ','santo' in inicio[0])