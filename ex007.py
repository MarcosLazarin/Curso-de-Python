a1 = float(input('Digite a nota do 1°bimestre: '))
a2 = float(input('Digite a nota de 2°bimestre: '))
m = (a1 + a2 * 2)/3
print('A sua média foi: {:.2f}'.format(m))
if m >= 5.5:
    print('Você foi aprovado! Parabéns!')
else:
    print('Você está reprovado, que pena!')
