#Escreva um programa que pergunte o salário de um funcionário.
#Calcule o valor de seu aumento.
#Para salários superiores a R$1.250,00 calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.
a = float(input('Qual é o seu salário: '))
s1 = a * 1.10
s2 = a * 1.15
if a > 1250:
    print('Seu salário que é {}, com o aumento de 10% passa a ser {}.'.format(a, s1))
else:
    print('Seu salário que era {}, com o aumento de 15% passou a ser {}.'.format(a, s2))
print('________________________________FIM________________________________________')