#Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado e a quantidade 
#de dias que ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 ao dia e 
#R$ 0,15 por km rodaddo 

dias = int(input('Informe por quantos dias o carro ficou alugado: '))
km = float(input('Agora informe quantos km percorreu: '))

qDia = 60 * dias
qKm = 0.15 * km

preço = qDia + qKm

#ou

#Preço = (60 * dias) + (0.15 * km)

print(f'O total a pagar é de R${preço:.2f}')