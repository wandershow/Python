#crie um programa que leia o nome completo e mostre:
# o nome com todas as letras maiusculas
# o nome com todas as letras minusculas
# quantas letras ao todo sem considerar espaços
#quantas letras tem o primeiro nome

nome = input('Digite seu nome e sobre nome: ')

print(nome.upper())
print(nome.lower())
print('total de letras sem espaços é: ', nome.__len__() - nome.count(' '))
primeiro = nome.split()
print('o primeiro nome tem:', primeiro[0].__len__(), 'letras')
