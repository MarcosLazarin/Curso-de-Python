#Fazer um programa que pergunte o sexo M ou F, e aceite sómente esses valores. Caso errado peça a digitação novamente.
sexo = input('Digite qual é o seu sexo: [M/F] ').upper().strip()[0]
while sexo not in 'MmFf':
    sexo = input('Dados inválidos, por favor insira novamente seu sexo: ').upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
