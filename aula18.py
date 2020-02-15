galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: '))) #aqui add no final da lista o 'nome'
    dado.append(int(input('Idade: '))) #aqui add no final da lista o 'idade'
    galera.append(dado[:]) #aqui add uma copia da ista dado no final da lista galera
    dado.clear() # aqui limpa a lista dado

for p in galera: # para cada pessoa na lista galera faça:
    if p[1] >= 21: # se pessoa na posição [1] mior ou igual a 21 faça:
        print(f'{p[0]} é maior de idade.') # mostre o nome é maior de idade
        totmai += 1
    else: # se nao for maior ou igual faça:
        print(f'{p[0]} é menor de idade.') # mostre o nome e menor de idade
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.') # mostra o total de cada.