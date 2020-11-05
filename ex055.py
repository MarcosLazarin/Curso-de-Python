#Faça um programa que leia o peso de 5 pessoas e no final, mostre qual foi o maior e o menor peso.
ma = 0
me = 0
for l in range(1, 7):
    peso = float(input('O peso da {} pessoa é: '.format(l)))
    if l == 1:
        ma = peso
        me = peso
    else:
        if peso > ma:
            ma = peso
        if peso < ma:
            me = peso
print('O maior peso é : {}'.format(ma))
print('O menor peso é: {}'.format(me))