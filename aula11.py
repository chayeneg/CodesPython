"""
Operadores Relacionais
==
>
>=
<
<=
!=
"""

nome = input('qual o seu nome? ')
idade = int(input('qual a sua idade? '))

idadeMenor = 20
idadeMaior = 30

if idade >= idadeMenor and idade <= idadeMaior:
    print(f'{nome} pode pegar emprestimo')
else:
    print(f'{nome} não pode pegar emprestimo')
