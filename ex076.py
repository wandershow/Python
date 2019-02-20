'''crie um programa que tenha uma unica tupla com nomes de produtos e seus respectivos preços na sequencia
no final mostre uma listagem de preços, organizando os dados em forma tabular...'''

produtos = ('Arroz', 2.90, 'Feijão', 4.50, 'Frango' , 10.90, 'Carne', 19.80, 'Sazon', 2)
print('-'*40)
print(f'{"LISTAGEM DE COMPRAS":^40}')
print('-'*40)
for c in range(0, len(produtos),2):
    print(f'{produtos[c]:.<30}R${produtos[c+1]:>7.2f}')
print('-'*40)