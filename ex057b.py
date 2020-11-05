#Fazer um programa que pergunte o sexo M ou F, e aceite sómente esses valores. Caso errado peça a digitação novamente.

sexo = input('Qual é o seu sexo? [M/F] ').upper().strip()
while sexo not in 'MmFf':
    sexo = input('Informação equivocada! \ninsira novamente: ').upper().strip()
print('Seu sexo {} foi inserido corretamente!'.format(sexo))