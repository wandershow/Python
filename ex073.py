#crie uma tupla preenchida com os 20 primeiros times em ordem de classificação do brasileirão 2018
#mostre os 5 primeiros
#os ultimos 4 da tabela
#uma lista com os times em ordem alfabetica
# em que posição esta o time da chapecoense

br = ('palmeiras', 'flamengo', 'inter', 'gremio', 'são paulo', 'atletico mg', 'atletico pr', 'cruzeiro', 'botafogo',
      'santos', 'bahia', 'fluminense', 'corinthians', 'chapecoense', 'ceara', 'vasco', 'sport', 'america',
      'vitoria', 'parana')

print(f'esses sao os 5 primeiros colocados{br[0:5]} ')
print(f'esses são os ultimos 4 colocados{br[16:]}') # pode ser tb {br[-4:]}
lista = sorted(br)
print(lista)
c = 0
while c < 20:
    if br[c] == 'chapecoense':
        print(f'A {br[c]} ficou na {c+1}º posição ')
    c += 1
print(f'A chapecoense ficou na {br.index("chapecoense")+1}ª posição.') # faz a mesma coisa que o de cima de uma
# maneira melhor, obs* tem que usar aspas duplas dentro do index, se não da erro ou usar o ".format"
