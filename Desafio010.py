#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 
#Considere US$ 1.00 = R$4.88

din = float(input('Informe quanto você possui na carteira: '))

conv = din / 4.88

print(f'Você pode comprar até {conv: .2f} dólares')