#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km a cima do limite.
a = float(input('Qual foi a velocidade do carro? '))
b = (a - 80) * 7.00
c = a - 80
if a > 80:
    print('Você foi multado por passa {}km a cima da velocidade. Gerando uma multa no valor de {} reais.'.format(c, b))
else:
    print('Você não foi multado, prossiga a viagem!')