'''Faça um programa que leia de 0 a 9999 e mostre na tela cada um dos digitos separados'''

numero = str(input('Informe um número: '))

dividido = numero.split()

print(f'Analisando o número {numero}')
print(f'Unidade: {dividido[4]}')
print(f'Dezena: {dividido[3]}')
print(f'Centena: {dividido[2]}')
print(f'Milhar: {dividido[1]}')