import pygame
from methods import load_image


class Object:
    def __init__(self, x: int, y: int):
        self.field_hitbox = pygame.rect.Rect(x, y, 100, 100)
        self.field_color = pygame.color.Color((153, 255, 51))

    def draw(self, screen: pygame.Surface, is_show_hitbox=True):
        if is_show_hitbox:
            pygame.draw.rect(screen, self.field_color, self.field_hitbox, width=2)


class Rock(Object):
    image = load_image("images/block.png")

    def __init__(self, x: int, y: int):
        super().__init__(x, y)

        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = Rock.image
        self.sprite.rect = self.field_hitbox
        self._ = pygame.sprite.GroupSingle()
        self._.add(self.sprite)

    def draw(self, screen: pygame.Surface, is_show_hitbox=True):
        self._.draw(screen)
        super().draw(screen, is_show_hitbox)