# refaça o ex035 mostrando que tipo de triangulo sera formado
# Equilatero = todos os lados iguais
# Isóceles = dois lados iguais
# Escaleno = todos os lados diferentes

a = int(input('digite o comprimento da 1º reta: '))
b = int(input('digite o comprimento da 2º reta: '))
c = int(input('digite o comprimento da 3º reta: '))

if (a < (b + c)) and (b < (c + a)) and (c < (a + b)):
    if a == b and a == c:
        print('Triangulo Equilatero')
    elif (a == b or a == c) or b == c:
        print('Triangulo Isoceles')
    else:
        print('Triangulo Escaleno')
else:
    print('Não é triangulo!!!')