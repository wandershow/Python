# faça um programa que leia 4 nomes e aleatoriamente crie uma lista organizada

from random import shuffle
n1 = input('digite o primeiro aluno: ')
n2 = input('digite o segundo aluno: ')
n3 = input('digite o terceiro aluno: ')
n4 = input('digite o quarto aluno: ')
lista =[n1, n2, n3, n4]
shuffle(lista)                # shuffle e uma função da biblioteca ramdom e serve para embaralhar uma lista

print('A ordem de apresentação sera !')
print(lista)
