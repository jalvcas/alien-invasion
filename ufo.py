import pygame

class Ufo:
    '''Clase para gestionar el platillo volador'''

    def __init__(self, ai_game):
        '''Inicializa el platillo volador y establece su posición inicial'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Carga la imagen del platillo volador y obtiene su rectángulo.
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        # Ubica el platillo volador en el centro de la pantalla.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        '''Dibuja el platillo volador en su posición actual'''
        self.screen.blit(self.image, self.rect)

    