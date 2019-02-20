# leia a largura e a altura de uma parede em metros e calcule sua area e quantidade
# de tinta necessaria para pinta-la, sabendo que cada itro de tinta, pinta uma area de 2m²

l = int(input('Qual a largura da parede em metros? '))
a = int(input('Qual a altura da parede em metros? '))

r = (l * a) / 2

print('A quantidade de tinta necessaria é de {} litros'.format(r))