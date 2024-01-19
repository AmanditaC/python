'''Crie um programa que leia o nome de uma pessoa e diga se tem Silva no nome'''

nome = str(input('Informe seu nome: ')).strip().upper()
nome = 'SILVA' in nome
print(f'Seu nome tem Silva? {nome}')