# leia uma frase pelo teclado, quantas vezes aparece a letra 'A', em que fosição ela aparece a primeira vez,
# em que posição ela aparece a ultima vez

frase = input('Digite uma frase: ').strip().lower()
print('aparecem {} letras "a"'.format(frase.count('a')))
print('A primeira vez e na posição :', frase.find('a')+1)
print('a ultima vez e na posição: ', frase.rfind('a')+1)