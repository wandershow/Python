'''Crie um  programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um
dicionario, se por a caso a CTPS for diferente de 0, o dicionário recebera tambem o ano de contratação e o salario.
calcule e acrescente, alem da idade com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime

pessoa = dict()
pessoa ['nome'] = str(input('Digite o nome: '))
nascimento = int(input('Digite o ano de nascimento: '))
pessoa ['idade'] = datetime.now().year - nascimento #aqui descobre a idade atual usando a função datetime.now().year
pessoa ['ctps'] = int(input(('Digite o numero de sua carteira de trabalho: (0 se nã tiver):')))

if pessoa['ctps'] != 0:
    pessoa ['contratacao'] = int(input('Digite o ano de contratação: '))
    pessoa ['salario'] = float(input('Digite o salario: '))
    pessoa ['aposentadoria'] = pessoa['contratacao'] - nascimento + 35
print('-='*30)
for k, v in pessoa.items():
    print(f'    - {k} tem o valor {v}')