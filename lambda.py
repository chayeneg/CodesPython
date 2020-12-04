lista = [
    ['p1', 13],
    ['p2', 18],
    ['p3', 5],
    ['p4', 3],
    ['p5', 50],
    ['p6', 1], 
]

print (sorted(lista, key=lambda i: i[1]))
print (lista)

#  a expressão lambda é uma espécie de função, porém sem nome. 
# Ela realiza cálculos, # filtros e retorna valores ou coleções 
# de valores.