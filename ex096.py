''' Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular(largura e
comprimento e mostre a area do terreno'''

def area(largura, comprimento):
    terreno = largura * comprimento
    print(f'A area de um terreno {largura:.2f}x{comprimento:.2f} é {terreno:.2f}m².')


print('Controle de terrenos')
print('-' * 40)
largura = float(input(f'Digite a largura (m): '))
comprimento = float(input(f'Digite o comprimento (m): '))
area(largura, comprimento)
