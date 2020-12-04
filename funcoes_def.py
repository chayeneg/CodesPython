# def funcao_ola(msg, nome):
#     print(msg, nome)
# funcao_ola('Olá', 'Mundo')

# def funcao_ola(msg='Olá', nome='usuário'):
#     nome = nome.replace('a', '3')
#     msg = msg.replace('u', '4') 
#     return f'{msg} {nome}'
# variavel = funcao_ola()
# print(variavel)

# def divisão(n1, n2):
#     if n2 == 0:
#         return
#     return n1/n2 
# divide = divisão(8,0)
# if divide:
#     print(divide)
# else: 
#     print('Conta inválida')

# Funções (def) em Python - *args  **kwargs

# def func(*args, **kwargs): 
#         print(args)
#         print(kwargs['nome'], kwargs['sobrenome'])
#         idade = kwargs.get('idade')
#         if idade is not None:  
#             print (idade)
#         else:
#             print ('Idade não existe')

# o * é como se fosse um empacotador, pode ser usado em casos onde 
# não se sabe a quantidade exata de argumentos (args) a serem passados 
# como parâmetro. 
# o kwargs possui a mesma função do args mas só para argumentos nomeados

# lista = [1, 2, 3, 4, 5]
# print (lista)
# func (*lista, nome='Chayene', sobrenome='Goncharenco', idade = 28) # lista desempacotada e sep(arada) por - sep='-'

