import pygame

class Object:
    def __init__(self, x: int, y: int):
        self.field_hitbox = pygame.rect.Rect(x, y, 100, 100)
        self.field_color = pygame.color.Color((153, 255, 51))

    def draw(self, screen: pygame.Surface, is_show_hitbox=True):
        if is_show_hitbox:
            pygame.draw.rect(screen, self.field_color, self.field_hitbox, width=2)