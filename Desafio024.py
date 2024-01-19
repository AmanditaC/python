'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome Santo'''

cid = str(input('Informe em que cidade vc nasceu: ')).strip().upper()

print('SANTO' in cid)