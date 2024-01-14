'''Crie um programa que leia o nome completo de uma pessoa e mostra:

1. O nome com todas as letras maiúsculas
2. O nome com todas minúsculas
3. Quantos letras ao todo (sem considerar espaços)
4. Quantas letra tem o primeiro nome'''

nome = str(input('Informe seu nome completo: ')).strip()

print(f'\nSeu nome em maiúsculo fica: {nome.upper()}')
print(f'\nSeu nome em minúsculo fica: { nome.lower()}')

'''nome = len(nome.replace(' ', ''))
print(f'\nSeu nome tem {nome} letras')'''

print(f'\nSeu nome tem {len(nome) - nome.count(" ")} letras')

separa = nome.split()
print(f'\nSeu primeiro nome tem {len(separa[0])} letras')