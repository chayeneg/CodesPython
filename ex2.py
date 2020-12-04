"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiiba a saudação apropriada. Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

horario = input('digite um horário (0-23): ')
if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('horario deve estar entre 0 e 23')
    else:
        if horario <=0:
            print('Bom dia')
        elif horario <=17:
            print('Boa tarde')
        else:
            print('Boa noite')
else:
    print('por favor, digite um horario entre 0 e 23')