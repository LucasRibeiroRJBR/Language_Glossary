import pygame

def play(audio):
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()


def dimensao(dim):
    # OBTENDO DIMENSÕES DO MONITOR
    monitor_largura = dim.winfo_reqwidth()
    monitor_altura = dim.winfo_reqheight()

    # OBTENDO LARGURA/ALTURA DO MONITOR E DA JANELA
    posicao_horizontal = int(dim.winfo_screenwidth()/2 - monitor_largura/2)
    posicao_horizontal = int(dim.winfo_screenheight()/2 - monitor_altura/2)

    # POSICIONANDO NO CENTRO DO MONITOR
    dim.geometry(f"+{posicao_horizontal}+{posicao_horizontal}")

    # MANTÉM A JANELA FOCADA
    dim.focus()