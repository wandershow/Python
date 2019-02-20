#Leia o nome de 4 alunos e mostre o sorteado na tela

from random import choice
n1 = input('digite o primeiro aluno: ')
n2 = input('digite o segundo aluno: ')
n3 = input('digite o terceiro aluno: ')
n4 = input('digite o quarto aluno: ')
lista =[n1, n2, n3, n4]
escolhido = choice(lista) # choice e uma função de random e serve para escolher aleatoriamene

print('O aluno escolhido foi {}'.format(escolhido))

