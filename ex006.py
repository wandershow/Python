
# Leia um numero mostre seu dobro, seu triplo e raiz quadrada
#para saber a raiz quadrada de um numero eleva-se "n ** (1/2)", se queres saber a raiz cubica eleva-se "n ** (1/3)"

n = int(input('Digite um numero: '))
print('O dobro de {}, é {}, o triplo é {}, e a raiz quadrada é {}'.format(n, n*2, n*3, n ** (1/2)))