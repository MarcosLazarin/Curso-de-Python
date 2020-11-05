# Criar um programa onde o usuário irá escrever uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses  abertos e fechados na ordem correta.

expressao = input('Digite a expressão: ')
lista = []
for elementos in expressao:
    if elementos =='(':
        lista.append('(')
    elif elementos == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está invalida!')