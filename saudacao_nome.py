# Exercicio 1
# crie uma função que exibe uma saudação com os parâmetros 
# saudação e nome

def saudacao(msg, nome):
    print(msg, nome) 

nome = input('Qual o seu nome? \n')
msg = ('Olá, ')

saudacao(msg, nome)