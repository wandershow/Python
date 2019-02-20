#Crie um programa que leia varios numeros inteiros pelo teclado. no final da execução, mostre a media entre todos os
# valores e qual foi o maior e o menor valor lidos. o programa deve perguntar ao usuario se ele quer ou não continuar
# a digitar valores
c = 'S'
media = 0
maior = 0
menor = 0
count = 0
while c == 'S':
    n = int(input('Digite o numero: '))
    count +=1
    media += n
    if count == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    c = str(input('Voce gostaria de continuar a digitar valores? [S/N]')).upper()
print('A média entre os {} valores digitados é de {:.2f}'.format(count, media/count))
print('O maior valor digitado é {}'.format(maior))
print('O menor valor digitado é {}'.format(menor))