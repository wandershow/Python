# Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base para
# conversão:
# 1 binario
# 2 octal
# 3 hexadecimal

numero = int(input('Digite o numero que você quer converter: '))
print(''' 
 Digite 1 para converter para binario
 Digite 2 para converter para octal 
 Digite 3 para converter  para hexadecimal ''')
n = int(input('Sua opção: '))
if n < 1 or n >3:
    print('Opção invalida!!')
elif n == 1:
    print('o numero binario de {} é {}'.format(numero, bin(numero)[2:])) # "[2:]" serve para mostrar a partir da 3º casa
elif n == 2:
    print('o numero octal de {} é {}'.format(numero, oct(numero)[2:]))
elif n == 3:
    print('o numero hexadecimal de {} é {}'.format(numero, hex(numero)[2:]))