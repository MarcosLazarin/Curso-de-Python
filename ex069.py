# Fazer programa que leia idade e sexo de várias pessoas.
# A cada pessoa cadastrada o computador deverá perguntar se quer continuar.
# No final, mostre:
# Quantas pessoas tem mais de 18 anos.
# Quantos homens foram cadastrados.
# Quantas mulheres tem menos de 20 anos.

from time import sleep
maiorde18 = sexohomem = sexomulher = mulhermenor = 0
print('=' * 40)
print('{:^40}'.format('CADASTRO DE PESSOAS'))
print('=' * 40)
while True:
    nome = input('Digite um nome: ').title()
    sexo = input('Digite o sexo: [M/F] ').upper().strip()
    while sexo not in 'FfMm':
        print('COMANDO NÃO IDENTIFICADO! \nPor favor digite o sexo novamente! ')
        sexo = input('Digite o sexo: [M/F] ').upper().strip()
    idade = int(input('Digite a idade: '))
    print('-' * 40)
    continuar = input('Você quer continuar? [S/N] ').upper().strip()
    if continuar == 'N':
        sleep(0.5)
        print('Ok, processando informação.')
        sleep(1)
    print('-' * 40)
    if idade > 18:
        maiorde18 += 1
    if sexo == 'M':
        sexohomem += 1
    elif sexo == 'F':
        sexomulher += 1
    if sexo == 'F' and idade < 20:
        mulhermenor += 1
    if continuar == 'N':
        break
sleep(1)
if maiorde18 == 1:
    print('Foram cadastradas 1 pessoa maior de 18 anos.')
    print('-' * 40)
elif maiorde18 == 0:
    print('Nenhuma pessoa maior de 18 anos foi cadastrada.')
    print('-' * 40)
elif maiorde18 > 1:
    print(f'Foram cadastradas {maiorde18} pessoas maiores de 18 anos.')
    print('-' * 40)
sleep(1)
if sexohomem == 0:
    print('Nenhum homem foi cadastrado.')
    print('-' * 40)
elif sexohomem == 1:
    print('Foi cadastrado 1 homem.')
    print('-' * 40)
elif sexohomem > 1:
    print(f'Foram cadastrados {sexohomem} homens.')
    print('-' * 40)
sleep(1)
if sexomulher == 0:
    print('Nenhuma mulher foi cadastrada.')
    print('-' * 40)
elif sexomulher == 1:
    print('Foi cadastrada 1 mulher.')
    print('-' * 40)
elif sexomulher > 1:
    print(f'Foram cadastradas {sexomulher} mulheres.')
    print('-' * 40)
sleep(1)
if mulhermenor == 0:
    print('Nenhuma mulher menor de 20 anos foi cadastrada.')
    print('-' * 40)
elif mulhermenor == 1:
    print('Foi cadastrada 1 mulher menor de 20 anos.')
    print('-' * 40)
elif mulhermenor > 1:
    print(f'Foram cadastradas {mulhermenor} mulheres menores de 20 anos.')
    print('-' * 40)
print('=' * 40)
print('{:^40}'.format('PROGRAMA ENCERRADO'))
print('=' * 40)