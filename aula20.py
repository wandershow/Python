#Funções
'''
def mostraLinha():  #sempre entre uma def e o programa principal tem que deixar 2 linhas vazias
    print('-'*50)


mostraLinha()
'''

'''def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


titulo('    CURSO EM VIDEO  ')
'''
'''
def soma(a, b):
    s = a+b
    print(s)


soma(4, 5) #posso apenas passar os parametros
soma(a=4, b=5) # posso passar atribuindo
soma(b=4, a=5) # posso passar atribuindo em ordem inversa desde que esteja explicito'''

#Empacotamento em python
#Quando eu não sei a quantidade de parametros que vao ser passados crio uma def nome(*num)
'''
def contador(*num): # ele vai criar uma tupla
    for v in (num):
        print(f'{v}', end='')
    print()


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''
'''
def contador(*num): # ele vai criar uma tupla
    tam = len(num)
    print(f'recebi os valores {num} e são ao todo {tam} numeros')

contador(3, 8, 0)'''

'''
def dobra(lista): # lista vai receber valores com vinculo, ou seja tudo que eu fizer em lista altera em valores
    pos = 0
    while pos < len(lista): # enquanto a posição menor que o tamanho da lista faça
        lista[pos] *= 2  #lista na posiça vai mutiplicar por 2 e assumir o resultado
        pos += 1   #incrementa a posição


valores = [6, 3, 9, 1, 0, 2]
dobra(valores) # aqui passa o metodo
print(valores) # [12, 6, 18, 2, 0, 4]'''