import pygame


class Enemy:
    def __init__(self, x: int, y: int):
        self.enemy_hitbox = pygame.rect.Rect(x, y, 90, 90)
        self.enemy_color = pygame.color.Color((127, 0, 255))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.enemy_color, self.enemy_hitbox, width=2)