def formatar_nome(nome_completo):
    nome_formatado = [nome.capitalize() for nome in nome_completo.split()]
    resultado = ' '.join(nome_formatado)
    resultado = resultado.replace(' Da ', ' da ').replace(' De ', ' de ')
    return resultado



"""
split retorna uma lista de strings
capitalize converte o primeiro caractere de uma string em letra maiúscula e minúscula em todos os outros caracteres, se houver
"""