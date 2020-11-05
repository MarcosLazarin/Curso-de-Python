#Desenvolver um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
#A média de idade do grupo;
#Qual é o nome do homem mais velho;
#Quantas mulheres tem menos de 20 anos.

from time import sleep
soma = 0
maioridadehomem = 0
nomevelho = ''
mulher = 0
for n in range(1, 5):
    sleep(1)
    print('----- {}ª PESSOA ------'.format(n))
    nome = input('Qual é o nome da {}ª pessoa: '.format(n))
    idade = int(input('Qual é a idade da {}ª pessoa: '.format(n)))
    sexo = input('Qual é o sexo (M ou F) da {}ª pessoa: ').upper().strip()
    soma = soma + idade
    if sexo == 'F' and idade < 20:
        mulher = mulher + 1
    if n == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
media = soma / 4
print('A idade do homem mais velho é {} anos e ele se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos de idade.'.format(mulher))
print('A média de idade do grupo é de {} anos'.format(media))

