from turtle import speed
import pygame


window = pygame.display.set_mode((300, 540))
largura_tecla = 165
altura_tecla = 260
tecla_comum = pygame.image.load('tecla comum.png')
tecla_arrastar_preta = pygame.image.load('tecla arrastar preta.png')
#carregar/desenhar retangulo

class Tecla(pygame.sprite.Sprite):
    def __init__(self, x, y, window):
        super(Tecla, self).__init__()

        self.img = tecla_comum 
        self.x, self.y = x, y
        self.window = window
        
        self.surface = pygame.Surface((largura_tecla, altura_tecla), pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_tecla(self):
        self.rect.y += speed
        if self.rect.y > 540:
            self.kill()

        pygame.draw.rect(self.surface, self.img,(0, 0, largura_tecla, altura_tecla))
        self.window.blit(self.surface, self.rect)


