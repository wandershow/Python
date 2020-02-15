'''ex094 unindo dicionarios e listas
 Crie um programa que leia nome, sexo e idade de varias pessoas, guardando dados de cada pessoa em um dicionario e
 todos dicionarios os dicioarios em uma lista.no final, mostre
 A) quantas pessoas cadastradas
 B) A media de idade
 C) Uma lista com mulheres.
 D) Uma lista com idade acima da media.
 '''

galera = list()   # cria lista
pessoa = dict()   # cria dicionario
soma = media = 0

while True: # enquanto for verdade faça:
    pessoa.clear() # aqui limpa o dionario
    pessoa['nome'] = str(input(('Nome: ')))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0] #le o sexo joga pra maiuscula e pega so a primeira letra.
        if pessoa['sexo'] in 'MF)':  # se o usuario digitar qualquer coisa diferente de M/F vai mostrar ERRO na tela
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy()) # aqui add uma copia do dicionario ao final da lista sem vinculo.
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0] #le a resp joga pra maiuscula e pega so a primeira letra
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='* 30)
print(f'A ) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A media de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end=', ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print(f'D) Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ', end=' ')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()
print('<< ENCERRADO >>')




