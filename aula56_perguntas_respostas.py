perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {'a':'1', 'b':'4', 'c':'6'},
        'resposta_certa': 'b',
    },
        'Pergunta 2': {
        'pergunta': 'Quanto é 2*6?',
        'respostas': {'a':'1', 'b':'4', 'c':'12'},
        'resposta_certa': 'c',
    },
}

print('Texto explicativo')
print()

respostas_certas = 0
for pergunta_chave, pergunta_valor in perguntas.items():
    print(f'{pergunta_chave}: {pergunta_valor["pergunta"]}')

    print('Respostas: ')
    for resposta_chave, resposta_valor in pergunta_valor['respostas'].items():
        print(f'[{resposta_chave}]: {resposta_valor}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pergunta_valor['resposta_certa']:
        print('Você acertou!')
        respostas_certas += 1
    else: 
        print('Você errou!')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')


print()