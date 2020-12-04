"""
CPF = 413.417.528-36

4*10 = 40           4*11 = 44
1*9 = 9             1*10 = 10  
3*8 = 24            3*9 = 27
4*7 = 28            4*8 = 32
1*6 = 6             1*7 = 7
7*5 = 35            7*6 = 42       
5*4 = 20            5*5 = 25
2*3 = 6             2*4 = 8
8*2 = 16            8*3 = 24
                    3*2 = 6

184                     225

11 - (184 % 11) = 11-8 = 3     11 - (225 % 11) = 11 - 5 
8 <= 9 = 3                    
Digito 1 = 3                   Digito 2 = 6

** se o resultado da conta for >= 9 recebe o valor de 0,
caso contrário deve manter o resultado da conta
"""

cpf = input('digite o seu cpf: \n')
novo_cpf = cpf[:-2] 
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf[index]) * reverso

    reverso -=1
    if reverso <2: 
        reverso = 11
        digito = 11 - (total % 11)

        if digito > 9:
            digito = 0
        total = 0
        novo_cpf += str(digito)

#impossibilita a validação de cpf que tenham numeros sequenciais
sequencia = novo_cpf  == str(novo_cpf[0]) * len(cpf)

if cpf == novo_cpf and not sequencia:
    print('Seu CPF é Válido')
else: 
    print('Seu CPF é Inválido')

