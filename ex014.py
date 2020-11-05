km = float(input('Qual a quantidade de km rodados? '))
d = int(input('Qual a quantidade de dias? '))
pt = (d * 60) + (km * 0.15)
print('O preço a pagar por {} dias e {}Km foi R${}'.format(d, km, pt))