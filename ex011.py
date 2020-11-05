l = float(input('Qual a largura da parede em metros: '))
a = float(input('Qual a altura da parede em metros: '))
ar = l * a
t = ar * 0.5
print('Considerando que usamos 1 litro de tinta para pintar uma parede de 2 metros quadrados! \nPara pintar uma área de {} metros quadrados é necessário {} litros de tinta'.format(ar, t))
