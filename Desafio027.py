'''Faça um programa que leia o nome completo de uma pessoa. Mostrando em seguida o seu primeiro e último
nome separadamente.
EX: Ana Maria de Souza

Primeiro: Ana
Último: Souza'''

nome = str(input('Informe seu nome: ')).strip()
div = nome.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {div[0]}')
#-1 pode ser utilizado para se referir ao último objeto de uma lista
print(f'Seu último nome é {div[-1]}')