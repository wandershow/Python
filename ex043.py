# leia a altura e peso de uma pessoa, e calcule seu imc, e mostre seu status

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura**2)

if imc < 18.5:
    print('Abaixo do peso, seu IMC é {:.2f}'.format(imc))
elif imc <= 25:
    print('Peso ideal, seu IMC é {:.2f}'.format(imc))
elif imc <= 30:
    print('sobrepeso, seu IMC é {:.2f}'.format(imc))
elif imc <= 40:
    print('Obesidade, seu IMC é {:.2f}'.format(imc))
else:
    print('Obesidade morbida, seu IMC é {:.2f}'.format(imc))