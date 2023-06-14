#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
#ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

'''n = float(input('Informe qualquer número real: '))

print(f'O número {n} a parte inteira é {n:.0f}')'''

#ou

'''from math import trunc

n = float(input('Informe um número real: '))

aprox = trunc(n)

print(f'O número {n} tem como parte inteira {aprox}')'''

#ou 

n = float(input('Informe um número real: '))

aprox = int(n)

print(f'O número {n} tem como parte interia {aprox}')