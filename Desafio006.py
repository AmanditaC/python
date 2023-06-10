#crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = float(input('Informe um número: '))

d = n * 2
t = n * 3
raiz = pow(n,0.5)

print(f'O dobro de {n} é {d}\nO triplo é {t}\nE a raiz é {raiz}')