import pygame


class Player:
    PLAYER_SPEED = 100
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.player_hitbox = pygame.rect.Rect(x, y, 90, 90)
        self.player_color = pygame.color.Color((0, 255, 0))

    def draw(self, screen: pygame.Surface, is_hitbox=True):
        if is_hitbox:
            pygame.draw.rect(screen, self.player_color, self.player_hitbox, width=2)

    def move(self, x, y):
        self.x += (x * Player.PLAYER_SPEED)
        self.y += (y * Player.PLAYER_SPEED)
        self.player_hitbox = pygame.rect.Rect(int(self.x), int(self.y) , 90, 90)