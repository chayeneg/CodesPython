"""
Iterando strings com while em python
"""

minha_string = 'o rato roeu a roupa do rei de roma.'
tamanho_string = len(minha_string)

print(minha_string[2])

print(minha_string.count('r') )

c = 0

nova_string = ''
while c < tamanho_string:
    if minha_string[c] == 'r':
        nova_string = nova_string + minha_string[c].upper()
    else:
        nova_string += minha_string[c]

    c +=1

print (nova_string)
    