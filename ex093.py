'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. o programa vai ler o nome do jogador e
quantas partidas ele jogou. depois vai ler a quantidade de gols feitos em cada partida. No final tudo isso sera
guardado em um dicionario, incluindo o total de gols feitos no campeonato'''

dados = dict()
dados ['nome'] = str(input('nome do jogador? '))
dados ['qtd jogos'] = int(input(f'quantos jogos o {dados["nome"]} jogou?'))
gol = list()
total = 0
for k in range(0, dados['qtd jogos']):
    gol.append(int(input(f'quantos gols na partida {k+1} ')))
    #total = total + dados [['gol'][k]]
dados ['gols'] = gol[:] # adicionando lista no dicionario sem criar vinculo (maneira correta)
dados ['total de gols'] = sum(gol[:])
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'    O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {dados["qtd jogos"]} partidas')
for k in range(0, dados['qtd jogos']):
    print(f'    Na partida {k+1}, fez {gol[k]} gols')
print(f'Foi um total de {dados["total de gols"]} gols')

''' # percorre a posiçao e o conteudo usando enumerate.
for i, v in enumerate(dados('gols')):
    print (f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dados["total de gols"]} gols')
'''