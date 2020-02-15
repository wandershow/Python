'''Crie um programa que tenha uma função fatorial() que receba dois parametros: o primeiro que indique o numero a
calcular e o outro chamado show, que sera um valor logico(opcional) indicando se sera mostrado ou não na tela o
processo de calculo fatorial.'''
def fatorial(n, show=False):
    """
    --> Calcula o fatorial de um numero.
    :param n: O numero a ser calculado
    :param show:(opcional) mostrar ou não a conta.
    :return: O valor do fatorial de um numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
        else:
            print(' = ', end='')
        f *= c
    return f

#Programa Principal

print(fatorial(5))
help(fatorial)