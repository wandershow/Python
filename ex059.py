# crie um programa que leia dois numeros e mostre um menu na tela
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos numeros
#[5] sair do programa
#seu programa devera realizar a operação solicitada em cada caso

n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))
opcao = 0
while opcao != 5:
    print('='*150)
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa''')
    print('=' * 150)
    opcao = int(input('Escolha sua opção: '))
    print('=' * 150)
    if opcao == 1:
        r = n1 + n2
        print('A soma de {} + {} = {}'.format(n1, n2, r))
    elif opcao == 2:
        r = n1 * n2
        print('A multiplicação de {} x {} é = {}'.format(n1, n2, r))
    elif opcao == 3:
        if n1 > n2:
            print('{} é o maior'.format(n1))
        elif n1 < n2:
            print('{} é o maior'.format(n2))
        else:
            print('São iguais')
    elif opcao == 4:
        print('Digite novos numeros!')
        n1 = int(input('Digite o 1º numero: '))
        n2 = int(input('Digite o 2º numero: '))
    elif opcao == 5:
        print('SAINDO')
    else:
        print('Opção Invalida!! Tente novamente')

    print('')
print('Você saiu!')