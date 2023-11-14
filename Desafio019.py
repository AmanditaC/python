'''Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido.'''

import random

nome1 = str(input('Primeiro nome: '))
nome2 = str(input('Segundo nome:'))
nome3 = str(input('Terceiro nome:'))
nome4 = str(input('Quarto nome: '))

#declarando uma lista

lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)

print(f'A pessoa escolhida foi {escolhido}')

'''Outra forma de fazer

from random import choice

nome1 = str(input('Primeiro nome:'))
nome2 = str(input('Segundo nome:))
nome3 = str(input('Tereceiro nome:))

lista = [nome1, nome2, nome3]
escolhido = choise(lista)

print(f'A pessoa escolhida foi {escolhido}')
'''