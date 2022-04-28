import pygame
from codigo_das_teclas import Tecla

pygame.init()
window = pygame.display.set_mode((300, 530))
pygame.display.set_caption("Fox Tiles")

tela_inicio = pygame.image.load('tela start redimensionada.png')
capa = pygame.image.load('fundo 1 redimensionado.png')

t = Tecla(10, 10, window)

jogo = True
while jogo:
    window.blit(capa, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False

        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jogo = False

    t.update()
    pygame.display.update()