#Programa que faz a leitura de uma data

dia = int(input('Qual é o dia?'))
mes = int(input('Qual é o mês?'))
ano = int(input('Qual é o ano?'))

#print('Você nasceu no dia', dia, 'de', mes, 'de', ano, ',correto?')

print('Você nasceu no dia {} de {} de {}, correto?'.format(dia, mes, ano))