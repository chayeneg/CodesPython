# Exercicio 3
# Fizz Buzz - Se o parâmetro de função for divisível por 3, 
# retorne fizz, se o parâmetro da função for divisivel por 5,
# retorne buzz. Se o parâmetro da função for divisível por 5 
# e 3, retorne  FizzBuzz, caso contrário, retorne o número 
# enviado

def divisivel(num):

    if num % 3 == 0 and num % 5 == 0:
        return f'Fizz Buzz, {num} é divisível por 3 e 5'
    if num % 3 == 0: 
        return f'Fizz, {num} é divisível por 3'
    if num % 5 == 0: 
        return f'Buzz, {num} é divisível por 5'
    return num

num = int(input('Digite um número: '))
result = divisivel(num)
print (result)