'''Faça um programa que leia uma frase pelo teclado e mostre:
* Quantas vezes aparece a letra A
* Em que posição ela aparece pela primeira vez
* Em que posição ela aparece pela última vez'''

frase = str(input('Digite uma frase: ')).upper()
print(f'A letra A aparece {frase.count('A')} na frase.')
print(f'A primeira letra A aparece na posição {frase.find('A')+1}')
#O rfind vai contar de trás pra frente
print(f'A última letra A aparece na posição {frase.rfind('A')+1}')
