'''Faça um programa que leia nome e media de uma aluno, guardando tambem a situação em um dicionario.
No final mostre o conteudo da estrutura na tela'''

boletin = {'nome': '', 'media': '', 'situacao': ''}
boletin['nome'] = str(input('Nome: '))
boletin['media'] = float(input(f'Média de {boletin["nome"]}:'))
if boletin['media'] >= 7:
    boletin['situacao'] = 'aprovado'
else:
    boletin['situacao'] = 'reprovado'

for k, v in boletin.items():
    print(f'    {k} é igual a {v}')

'''print(f' Nome é igual a {boletin["nome"]}')
print(f'    Média é igual a {boletin["media"]:.1f}')
print(f'    Situação é igual a {boletin["situacao"]}')'''