'''Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
no final mostre um boletin contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno
individualment2'''

boletim = list()
nota = list()
aluno = list()
while True:
    nome = str(input('Nome do aluno: '))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    aluno.append(nome)
    aluno.append(nota[:])
    boletim.append(aluno[:])
    p = str(input('VOCÊ DESEJA CONTINUAR? [S/N]'))
    nota.clear()
    aluno.clear()
    if p in 'Nn':
        break
print('-='*30)
print(f'{"Nº":<4}{"Nome":<10}{"Media":>8}')
for n in range(0, len(boletim)):
    print(f'{n:<4} {boletim[n][0]:<10}{(boletim[n][1][0] + boletim[n][1][1])/2:>8.1f}')
print('-'*60)
r = 0
while True:
    print('-'*60)
    r = int(input('Qual aluno você deseja ver as notas? ou digite 999 para sair'))
    if r == 999:
        break
    print(f'Notas de {boletim[r][0]} São {boletim[r][1]}')

print('-'*60)