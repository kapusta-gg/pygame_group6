import pygame


class Room:
    def __init__(self):
        self.field = Field()


class Door: # Пока не трогаем
    pass


class Field:
    def __init__(self):
        self.field_hitbox = pygame.rect.Rect(100, 100, 800, 600)
        self.field_color = pygame.color.Color((0, 255, 0))

    def draw(self, screen):
        pygame.draw.rect(screen, self.field_color, self.field_hitbox, width=5)
