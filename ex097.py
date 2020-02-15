'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parametro e mostre uma
mensagem com tamanho adaptavel.'''
def lin(t):
    print('~' * t)


def escreva(txt):
    lin(len(txt))
    print(txt)
    lin(len(txt))


escreva('  CURSO EM VIDEO  ')
escreva(' PYTHON ')
escreva(' Hello world ')