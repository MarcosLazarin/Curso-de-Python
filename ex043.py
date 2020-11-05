# Escreva um programa que leia peso e altura de uma pessoa, calcule seu IMC e mostre seu status:
# 1) Abaixo de 18.5 = Abaixo do peso
# 2) Entre 18.5 e 25 = Peso ideal
# 3) 25 a 30 = Sobrepeso
# 4) 30 a 40 = Obesidade
# 5) Acima de 40 = Obesidade Mórbida
altura = float(input('Qual é a sua altura? '))
peso = float(input('Qual é o seu peso? '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.3f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 < imc < 25:
    print('Você está no peso ideal!')
elif 25 < imc < 30:
    print('Você está com sobrepeso!')
elif 30 < imc < 40:
    print('Você está obeso!')
else:
    print('Você está obeso mórbido!')