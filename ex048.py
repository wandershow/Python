#Faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de de tres e que se encontram
# no intervalo entre 1 e 500
n = 0
for c in range(1, 501, 2):
    if (c % 3) == 0:
        n += c
print(n)