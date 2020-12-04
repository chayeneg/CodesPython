# Exercicio 3
# Crie uma função que receba 2 números. O primeiro é um valor
# e o segundo um percentual (ex: 10%). Retorne (return) o 
# valor do primeiro somado do aumento percentual do mesmo

def percentual(valor, perc): 
    return valor + valor * (perc / 100)

valor = int (input('Digite o valor: '))
perc = int (input('Digite a porcentagem número: '))

valor_total = percentual(valor, perc)
print(valor_total)