"""
Manipulando strings
- Strings indices
- Fatiamento de strings [inicio:fim:passo]
- Funções built-in len, abd, type, print, etc...

Essas funções podem ser usadas diretamente em cada tipo.
"""

#positivos      [012345678]
texto          ='Python s2'
#negativos     -[987654321]

# FATIAMENTO DE STRINGS

# imprime do caractere 2 até o 6-1
# nova_string = texto[2:6] 

# imprime excluindo a partir do caractere -2
# nova_string = texto[:-2]  

# imprime passando de 2 em 2
nova_string = texto[0::2]  

print(nova_string)


