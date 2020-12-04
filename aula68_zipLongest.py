# zip - unindo iteraveis
# zip_longest - itertools

from itertools import zip_longest, count

indice = count()

## cidades
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']

## estados
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(indice, estados, cidades)

## cidades_estados_zip = zip(indice, estados, cidades)
## print(list(cidades_estados_zip))

## Saída: [('SP', 'São Paulo'), ('MG', 'Belo Horizonte'), ('BA', 'Salvador'), (None, 'Monte Belo'), (None, 'Outra')]

## cidades_estados = ziplongest(estados, cidades)
## print(list(cidades_estados_zipLongest)) 

## Saída: [('SP', 'São Paulo'), ('MG', 'Belo Horizonte'), ('BA', 'Salvador')]

for indice, estados, cidades in cidades_estados:
    print(indice, estados, cidades)