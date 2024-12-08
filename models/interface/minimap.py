import pygame


class MiniMap:
    def __init__(self):
        self.map = pygame.rect.Rect(800, 0, 200, 200)
        self.map_color = pygame.color.Color((255, 255, 255))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.map_color, self.map, width=2)