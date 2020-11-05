# Escreva um programa que leia duas notas de um aluno e escreva uma mensagem de acordo:
# 1) Média abaixo de 5 = reprovado
# 2) Média entre 5 e 6.9 = recuperação
# 3) Média 7 ou superior = aprovado

n1 = float(input('Qual foi a nota da A1: '))
n2 = float(input('Qual foi a nota da A2: '))
media = ((n1 * 1) + (n2 * 2)) / 3
if media < 5:
    print('Você foi reprovado! Sua média foi {:.3f}.  Infelizmente!!'.format(media))
elif 5 < media < 6.9:
    print('Você está de recuperação.\nSua média foi {:.3f}. \nFaça a prova final no dia que for marcado.'.format(media))
else:
    print('Parabéns, você foi aprovado! \nSua média foi {:.3f}.'.format(media))