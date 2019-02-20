# Crie um programa que leia uma frase qualquer e diga se ela e um palindromo desconsiderando os espaços

frase = input('Digite uma frase: ').strip().lower()
palavra = frase.replace(' ','') #aqui eu tirei os espaços da frase
inverso = palavra[::-1]  # aqui pega a palavra na ordem inversa sem precisar fazer o for decrecente
'''inverso =''
for c in range(len(palavra)-1, -1, -1): # aqui eu coloquei a palavra na ordem inversa
    inverso += palavra[c]'''
if inverso == palavra:
    print('{} é palindromo'.format(frase))
else:
    print('{} não é palindromo'.format(frase))
