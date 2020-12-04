"""
While
Utilizado para realizar ações enquanto uma condição for verdadeira
"""

while True:
    print()
    num1 = input('digite um numero: ')
    num2 = input('digite outro numero: ')
    operador = input('digite um operador: ')
    sair = input('deseja sair? [s]im ou [n]ão')

    if sair == 's':
        break
    
    if not num1.isnumeric() or not num2.isnumeric(): # verifica se a entrada do usuário é numero e, caso não seja, imprime na tela a msg avisando que precisa ser 
        print('voce precisa digitar um numero.')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        print(num1 / num2)
    elif operador == '*':
        print(num1 * num2)
    else:
        print('operador invalido.')
