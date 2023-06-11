#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preço = float(input('Informe o preço do produto: '))

des = (5/100) * preço

Npreço = preço - des

print(f'\nCom um desconto de 5% seu produto ficar por {Npreço}')