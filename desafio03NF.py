#Programa que informa qual é a soma de dois números e mostra o seu resultado

#Declarando uma variável e informando o tipo e lendo o valor que será digitado pelo usuário
numero1 = int(input('Digite um valor:'))
numero2 = int(input('Digite outro valor:'))
#Declarando uma variável que irá receber a soma dos dos números lidos anteriormente
soma = numero1 + numero2

#print('O valor da soma é {}!'.format(soma))

#Mostrando o valor dos números informados pelo usuário e a soma dos mesmos
print('O valor da soma entre {} e {}, é {}'.format(numero1, numero2, soma))