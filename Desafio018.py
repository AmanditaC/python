'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo'''

import math

n = float(input('Informe um ângulo: '))

sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))

print(f'O ângulo {n} tem como seno {sen:.2f}, cosseno {cos:.2f} e tangente {tan:.2f}')