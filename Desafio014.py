#Escreva um programa que converta uma temperatura digitada em °C e converta para °F

cel = float(input('Informe a temperatura em °C: '))

fa = cel * 1.8 + 32

#fa = ((9 * cel) / 5) + 32

print(f'A temperatura de {cel:.1f} °C é {fa:.1f} °F (Fahrenheit) ')