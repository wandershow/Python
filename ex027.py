# faça um programa que leia um nome completo e mostre o primeiro e ultimo nome separadamente

n = input('Digite um nome: ').strip()
print(n)
nome = n.split()

print('primeiro nome: {}'.format(nome[0]))

print('ultimo nome: {}'.format(nome[-1]))

print('ultimo nome: {}'.format(nome[len(nome)-1])) #outra maneira de mostrar o ultimo nome...
