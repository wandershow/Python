# leia 3 numeros e mostre o maior e o menor

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if (n1 > n2 and n1 > n3) :
    print('{} é o maior'.format(n1))
elif n2 > n1 and n2 > n3:
    print('{} é o maior'.format(n2))
else:
    print('{} é o maior'.format(n3))

if (n1 < n2 and n1 < n3) :
    print('{} é o menor'.format(n1))
elif n2 > n1 and n2 > n3:
    print('{} é o menor'.format(n2))
else:
    print('{} é o menor'.format(n3))

