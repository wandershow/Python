# Leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. se o valor digitado for impar
# desconsidere -o.
s = 0
for c in range(0, 6):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        s += n
print('A soma de todos os numeros pares é: {}'.format(s))
