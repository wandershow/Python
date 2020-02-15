'''Aprimore o desafio 093 para que ele funcione com varios jogadores, incluindo um sistema de visualização de
detalhes do aproveitamento cada jogador'''
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear() # limpando dicionario jogador pq fica lendo em looping
    jogador['nome'] = str(input('nome do jogador? '))
    tot = int(input(f'quantos jogos o {jogador["nome"]} jogou? '))
    partidas.clear() # limpando lista partidas pq esta sendo lido em looping
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]                    # adicionando lista no dicionario sem criar vinculo (maneira correta)
    jogador['total'] = sum(partidas)                 # aqui faz o somatorio de gols
    time.append(jogador.copy())                      # adicionando dicionario na lista de maneira correta
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda S ou N.')
    if resp == 'N':
        break

# Abaixo estamos fazendo o cabeçalho do que iremos mostrar
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)

# Aqui vai percorrer cada posição da lista time, e percorrer cada valor dentro de cada posição
for k, v in enumerate(time): # aqui pega a posição 'k' e o valor 'v'
    print(f'{k:>3} ', end='') # vai mostrar a coluna "cod" com 3 caracteres centralizado a direita -> {k:>3}
    for d in v.values(): # para cada valor 'd' in v.values
        print(f'{str(d):<15}', end='') # tem que passar o str pois nao aceita se for numerico
    print()
print('-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-'*40)
print('<< VOLTE SEMPRE >>')

