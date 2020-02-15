'''crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha separado os valores pares e impares.
no final mostre os valores pares e impares em ordem crescente'''

valores = [[], []]

for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º valor : '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)

print('-='*30)
print(f'Valores par {sorted(valores[0])} ')
print(f'Valores impar {sorted(valores[1])} ')