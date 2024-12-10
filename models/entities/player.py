import pygame


class Player:
    def __init__(self, x: int, y: int):
        self.player_hitbox = pygame.rect.Rect(x, y, 90, 90)
        self.player_color = pygame.color.Color((0, 255, 0))

    def draw(self, screen: pygame.Surface, is_hitbox=True):
        if is_hitbox:
            pygame.draw.rect(screen, self.player_color, self.player_hitbox, width=2)