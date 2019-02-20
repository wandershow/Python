n1 = int(input('um valor '))
n2 = int(input('outro valor '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# para na quebrar a linha colocamos "end=' '"
# para quebrar a linha colocamos " \n " para nao precisar fazer varios prints...

print('A soma é {}, o produto é {}, e a divisão é {:.3f}'.format(s, m, d), end=', ')
print('Divisão inteira {}, \n e potencia {}'.format(di, e))