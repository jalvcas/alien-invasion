import pygame

class Ship:
    '''Clase para gestionar la nave espacial'''

    def __init__(self, ai_game):
        '''Inicializa la nave espacial y establece su posición inicial'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Carga la imagen de la nave espacial y obtiene su rectángulo.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Ubica la nave en la parte inferior centro de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

        # Almacena un valor decimal para la posición horizontal de la nave.
        self.x = float(self.rect.x)

        # Bandera de movimiento; la nave no se mueve inicialmente.
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        '''Dibuja la nave en su posición actual'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Actualiza la posición de la nave según la bandera de movimiento."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Actualiza el rectángulo de la nave con su nueva posición self.x
        self.rect.x = self.x
    
    

    