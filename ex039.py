# Escreva um programa que leia o ano de nascimento de uma pessoa de acordo com sua idade e diga:
# Se ele ainda vai se alistar ao serviço militar
# Se é hora de se alistar
# Se já passou o tempo de alistamento
# O programa deve identificar quanto tempo falta ou passou de se alistar.

from datetime import date
idade = int(input('Qual é a sua idade? '))
b = date.today()
c = b.year
nascimento = c - idade
if 18 > idade > 16:
    print('O seu ano de nascimento é {} e você não está na hora de se alistar!'.format(nascimento))
    print('Falta 1 ano para o seu alistamento.')
elif idade < 18:
    print('O seu ano de nascimento é {} e você não está na hora de se alistar!'.format(nascimento))
    print('Faltam {} anos para o seu alistamento.'.format(18 - idade))
    print('Seu alistamento deve ocorrer em {} anos.'.format(nascimento + 18))
elif 20 > idade > 18:
    print('Seu ano de nascimento é {} e você já se alistou!'.format(nascimento))
    print('Você se alistou à exatamente 1 ano atrás, que foi em {}.'.format(c - 1))
elif idade > 18:
    print('Seu ano de nascimento é {} e você já se alistou!'.format(nascimento))
    print('Você se alistou à {} anos atrás, que foi em {}.'.format(idade - 18, nascimento + 18))
else:
    print('Seu ano de nascimento é exatamente {}.'.format(nascimento))
    print('Você deve se alistar IMEDIATAMENTE!')