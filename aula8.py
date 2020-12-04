"""
criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa
criar váriavel com o ano atual (int)
obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
obter o imc da pessoa com 2 casas decimais (peso e na altura da pessoa)
exibir um texto com todos os valores na tela usando F-String (com chaves)
"""
nome = 'Chayene' #string
idade = 28 # inteiro
altura = 1.63 # float
e_maior = idade > 18 # booleano
peso = 74 # inteiro
imc = (peso/(altura**2))
anoNasc = 2019 - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {anoNasc}')
