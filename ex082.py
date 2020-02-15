''' Crie um programa que vai ler varios numeros e colocar em uma lista
Depois disso crie duas listas extras que vão conter os valores par e impar separados
ao final mostre as 3 listas
'''
valores = list()
par = list()
impar = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    pergunta = str(input('Voce que continuar ? [S/N]')).upper()
    while pergunta != 'S' and pergunta != 'N':
        pergunta = str(input('Valor invalido!! Voce que continuar ? [S/N]')).upper()
    if pergunta == 'N':
        break
for c in range(0, len(valores)):
    if valores[c] % 2 == 0:
        par.append(valores[c])
    else:
        impar.append(valores[c])
print(f'os valores digitados foram {valores}')
print(f'os valores par digitados foram {par}')
print(f'os valores digitados impar foram {impar}')