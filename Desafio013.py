#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salário = float(input('Informe seu salário atual: '))

aum = salário * 1.15

print(f'Com um aumento de 15% seu novo salário agora passa a ser de {aum:.2f}')