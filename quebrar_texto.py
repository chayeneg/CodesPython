def quebrar_texto(frase):
    if len(frase) > 15: 
        return frase[:12] + '...'
    else: 
        return frase