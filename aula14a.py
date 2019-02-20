c = 1
while c < 10:  # usar o while quando nao souber a quantidade de repetiçoes necessarias
    print(c)
    c+= 1
print('fim')

r = 'S'
while r == 'S':
    n = int(input('digite um numero: '))
    r = str(input('Quer continuar ? [S/N]')).upper()
print('fim')