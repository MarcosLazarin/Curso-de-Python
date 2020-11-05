#Escreva um programa que pergunte a distância de uma viagem em KM:
#Calcule o preço da passagem, cobrando 0,50 centavos por KM para viagens até 200km e 0,45 para viagens mais longas.
d = int(input('Qual foi distância percorrida em Km? '))
if d <= 200:
    print('A distância percorrida foi {}, e você irá pagar R${:.2f} reais.'.format(d, (d*0.45)))
else:
    d >= 200
    print('A distância percorrida foi {}, e você terá que pagar R${:.2f} reais.'.format(d, d*0.50))