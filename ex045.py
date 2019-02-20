# crie um programa que faça o computador jogar jokempo ( pedra, papel, tesoura
from random import choice
from time import sleep
jogador = int(input('Escolha:\n0- PEDRA\n1- PAPEL\n2- TESOURA\nSua opção: '))
'''if n == 1:
    jogador = 'PEDRA'
elif n == 2:
    jogador = 'PAPEL'
elif n == 3:
    jogador = 'TESOURA' '''

tipo = ('PEDRA','PAPEL','TESOURA')
jokempo = choice(tipo)
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO')

print('='*150)
print('O COMPUTADOR JOGOU {}'.format(jokempo))
print('VOCE JOGOU {}'.format(tipo[jogador]))
print('='*150)

if(tipo[jogador]=='PEDRA' and jokempo=='PEDRA') or (tipo[jogador]=='PAPEL' and jokempo=='PAPEL') or (tipo[jogador]=='TESOURA' and jokempo =='TESOURA'):
    print('empate')
elif(tipo[jogador]=='PEDRA' and jokempo=='PAPEL') or (tipo[jogador]=='PAPEL' and jokempo =='TESOURA') or (tipo[jogador]=='TESOURA' and jokempo =='PEDRA'):
    print('Computador ganhou!!!')
elif(tipo[jogador] =='PAPEL' and jokempo =='PEDRA') or (tipo[jogador]=='PEDRA' and jokempo =='TESOURA') or (tipo[jogador]=='TESOURA' and jokempo =='PAPEL'):
    print('Voce ganhou!!!')
