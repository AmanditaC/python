'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, 
calcule e mostre o comprimento da hipotenusa.'''

from math import hypot

ca = float(input('Informe o valor do cateto adjacente: '))
co = float(input('\nInforme agora o valor do cateto oposto: '))

h = hypot(co, ca)

print(f'\nO comprimento da hipotenusa é de {h:.2f}')