# Escreva um programa que leia o ano de nascimento de um atleta e mostre sua categaria, de acordo:
# 1)Até 9: MIRIM
# 2)Até 14: INFANTIL
# 3)Até 19: JÚNIOR
# 4)Até 20:SÊNIOR
# 5)Acima: MASTER

from datetime import date
nasc = int(input('Qual é o ano do seu nascimento: '))
hoje = date.today()
ano = hoje.year
idade = ano - nasc

if idade <= 9:
    print('Você tem apenas {} anos.'.format(idade))
    print('Ah velho, você é MIRIM. Sai Fora!')
elif 10 < idade < 14:
    print('Você tem {} anos.'.format(idade))
    print('Você é um JUVENIL, Não falo com JUVENIL. THAU!')
elif 15 < idade < 19:
    print('Você tem {} anos.'.format(idade))
    print('Você é um JÚNIOR, está ganhando experiência!!')
elif idade == 20:
    print('Você tem {} anos.'.format(idade))
    print('Você é um SÊNIOR, tem muita moral por aqui!!')
else:
    print('Você tem {} anos.'.format(idade))
    print('Sua experiência é admirirável, você é um MASTER. A seu dispor!!')