#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n = float(input('informe um valor em metros: '))

cm = n * 100
mm = n * 1000

print(f'O valor convertido é o seguinte:\nEm centímetros é {cm}cm\nE em milímetros é {mm}mm')