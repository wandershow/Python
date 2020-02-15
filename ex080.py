'''Crie um programa onde o usuario possa digitar 5 valores numericos e cadastre-os em uma lista, ja na posição
correta de inserçao (Sem usar o sort()) no final mostre a lista ordenada na tela'''

valores = list()
cont = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('foi adicionado no final da lista ')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {valores}')
