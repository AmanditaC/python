#Faça um programa que leia algo pelo teclado e mostra na tela seu tipo primitivo e todas as infomações 
#possíveis sobre ele

algo = input ('Digite algo: ')

#print('O tipo primitivo é ', type(algo))
#print('Só tem espaços? ', algo.isspace())
#print('É um número? ', algo.isnumeric())
#print('É alfanumérico? ', algo.isalnum())
#print('É alfabético? ', algo.isalpha())
#print('Está em maiúsculo? ', algo.isupper())
#print('Está em minuscúla? ',algo.islower())
#print('Está capitalizada? ', algo.istitle())

print(f'O tipo de é {type(algo)}')
print(f'Só tem espaços? {algo.isspace()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em maiúsculo? {algo.isupper()}')
print(f'Está em minuscúla? {algo.islower()}')
print(f'Está capitalizada? {algo.istitle()}')