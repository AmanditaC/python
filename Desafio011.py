#Faça um programa que leia a largura e a altura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta necessária para pinta-lá, 
#sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

área = largura * altura 

litros = área / 2

print(f'Para uma área de {área:.1f} m2, você irá precisar de {litros:.1f} litros de tinta')