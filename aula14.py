"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiro (int)
:f - Números de ponto flutuante (float)
:.(Numero)f - quantidade de casas decimais (float)
:(Caractere)(> ou < ou ^)(Quantidade)(Tipo -s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print('{:.2f}'.format(divisao)) # formatando para 2 casas decimais com o :.2f

print(f'{divisao:.2f}')  # formatando para 2 casas decimais com o :.2f

nome = 'chayene'
# print(f'{nome:*^4}') # caso a quantidade do caractere a ser inserida com o nome seja <= ao tamanho do valor da variavel, não será inserido nenhum caractere

# quantidade  do caractere a ser inserido deve ser maior pq o calculo é feito: tamanho da variavel - quantidade de caractere a ser inserido = quantidade inserida. (ana - **** = ana*)
sobrenome = 'goncharenco'
nomeFormatado = '{0:*>60} {1:@>60}'.format(nome, sobrenome)
print(nomeFormatado)

print(nome.lower()) # tudo minusculo
print(nome.upper()) # tudo maiusculo
print(nome.title()) # primeiras letras maiusculas