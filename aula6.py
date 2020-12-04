"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Chayene' #string
idade = 28 # inteiro
altura = 1.63 # float
e_maior = idade > 18 # booleano
peso = 74 # inteiro
imc = (peso/(altura**2))

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)
print('Peso:', peso)
print('IMC:', imc)

print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)

