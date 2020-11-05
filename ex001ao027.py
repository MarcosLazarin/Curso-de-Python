#Programa que lê e interage com seu nome.
nome = input('Digite seu nome: ')
print('UAl, {} né, é um nome muito bonito, estou apaixonada com seu nome!'.format(nome))

#Programa que mostra o antecessor e sucessor de um número.
n1 = int(input('Digite um número: '))
print('O antecessor de {} é: {}'.format(n1, (n1 - 1)))
print('O sucessor de {} é: {}'.format(n1, n1 + 1))

#Programa que mostra o dobro, o triplo e a raiz de um número
n1 = float(input('Digite um número: '))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)
print('O dobro de {} é igual a: {} \nO triplo de {} é igual a: {} \nA raiz de {} é igual a: {:.2f}'.format(n1, d, n1, t, n1, r))

#Programa que mostra se você foi aprovado ou não.
a1 = float(input('Digite a nota do 1°bimestre: '))
a2 = float(input('Digite a nota de 2°bimestre: '))
m = (a1 + a2 * 2)/3
print('A sua média foi: {:.2f}'.format(m))
if m >= 5.5:
    print('Você foi aprovado! Parabéns!')
else:
    print('Você está reprovado, que pena!')

#Programa que lê um tamanho em metros e mostra os centímetros.
m = int(input('Digite um tamanho em metros: '))
c = m * 100
mi = m * 1000
print('{} metros é igual {} centímetros. \n{} metros é igual a {} milímetros.'.format(m, c, m, mi))

#Programa que mostra a tabuada de um número.
n1 = int(input('Digite um número que você queira saber a tabuada: '))
print('_'*12)
d0 = n1 * 0
d1 = n1 * 1
d2 = n1 * 2
d3 = n1 * 3
d4 = n1 * 4
d5 = n1 * 5
d6 = n1 * 6
d7 = n1 * 7
d8 = n1 * 8
d9 = n1 * 9
print('5x0={} \n5x1={} \n5x2={} \n5x3={} \n5x4={} \n5x5={} \n5x6={} \n5x7={} \n5x8={} \n5x9={}'.format(d0, d1, d2, d3, d4, d5, d6, d7, d8, d9))
print('_'*12)

#Programa que transforma seu dinheiro em dólar e euro.
re = float(input('Quanto de dinheiro você tem na carteira agora: R$'))
d = re / 5.38
e = re / 6.07
print('R${} reais é igua a: US${:.2f} \n{}reais é igual a: {:.2f}'.format(re, d, re, e))

#Programa para pintar parede
l = float(input('Qual a largura da parede em metros: '))
a = float(input('Qual a altura da parede em metros: '))
ar = l * a
t = ar * 0.5
print('Considerando que usamos 1 litro de tinta para pintar uma parede de 2 metros quadrados! \nPara pintar uma área de {} metros quadrados é necessário {} litros de tinta'.format(ar, t))

#Programa para calcular produto com 5% de desconto.
p = float(input('Digite o preço do produto: '))
d = p * 0.95
print('O preço do produto com 5% de desconto é {:.3f} reais'.format(d))

#Programa para calcular salário com 15% de aumento.
s = float(input('Digite o salário: R$'))
sa = s * 1.15
print('O salário com 15% de aumento é igual a:R${:.3f}'.format(sa))

#Programa para transformar °C em °F.
c = float(input('Digite um temperatura em °C: '))
f = ((9 * c) / 5) + 32
print('A temperaturade de {}°C corresponde a {}°F'.format(c, f))

#Programa para ler seno, cosseno e tangente.
import math
a = float(input('Digite um ângulo: '))
s = math.sin(math.radians(a))
print('Seno: {:.2f}'.format(s))
c = math.cos(math.radians(a))
print('Cosseno: {:.2f}'.format(c))
t = math.tan(math.radians(a))
print('Tangente: {:.2f}'.format(t))

#Programa para escolher um aluno entre 4.
import random
print('Este programa irá mostrar o sorteamento de 1 entre 4 alunos ')
n1 = str(input('1°aluno: '))
n2 = str(input('2°aluno: '))
n3 = str(input('3°aluno: '))
n4 = str(input('4°aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi o {}'.format(escolhido))

#Programa para ler unidade, dezena, centena e milhar.
num = str(input('Digite um número de 0 a 9999: ')).strip()
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Centena: {}'.format(num[0]))

#Programa para ler a frase.
frase = str(input('Digite uma frase: ')).strip().upper()
print('Esta frase tem {} letras "a". '.format(frase.count('A')+1))
print('A primeira vez que a letra "a" aparece é na posição {}.'.format(frase.find('A')))
print('A última vez em que a letra "a" aparece é na posição {}.'.format(frase.rfind('A')))

#Programa para ler nome.
nome = str(input('Digite seu nome: ')).strip()
s = nome.split()
print('Seu primeiro nome é {}'.format(s[0]))
#print('Seu último nome é {}'.format(s[len(s)-1]))
print('Seu último nome é {}'.format(s[-1]))