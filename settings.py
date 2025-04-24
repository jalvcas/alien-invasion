class Settings:
    """Clase para almacenar y gestionar configuraciones del juego."""

    def __init__(self):
        """Inicializa las configuraciones del juego."""
        # Configuraciones de la pantalla.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.sky_blue_color = (207, 236, 247)  # Color azul cielo
        self.ship_speed = 1.5
