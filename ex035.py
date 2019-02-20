# leia tres o comprimento de 3 retas e diaga ao usuario se elas podem ou não formar um triangulo

a = int(input('digite o comprimento da 1º reta: '))
b = int(input('digite o comprimento da 2º reta: '))
c = int(input('digite o comprimento da 3º reta: '))

if (a < (b + c)) and (b < (c + a)) and (c < (a + b)):
    print('é triangulo')
else:
    print('nao e triangulo')