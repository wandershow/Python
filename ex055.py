# Faça um programa que leia o peso de 5 pessoas, no final mostrar o maior e o menor peso

maior = 0
menor = 0
for c in range(0, 5):
    p = float(input('Digite o seu peso: '))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('{:.2f}kg é o maior peso!'.format(maior))
print('{:.2f}kg é o menor peso!'.format(menor))
