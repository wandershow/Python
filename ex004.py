dado = input('Digite algum dado : ')
print('O tipo primitivo desse dado é ', type(dado))
print(bool(dado))
print('e um numero', dado.isnumeric())
print('e alfa numerico ', dado.isalnum())
print('e alfabetico ?', dado.isalpha())
print('e decimal?', dado.isdecimal())
print('esta em minusculas', dado.islower())
print('esta em maisuculas ', dado.isupper())
print('esta capitalizada', dado.title())
print('tem apenas um digito?', dado.isdigit())
print('e mostravel?', dado.isprintable())


