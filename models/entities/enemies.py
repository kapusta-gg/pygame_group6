import pygame
from methods import load_image


class Enemy:
    SPEED = 50

    # scale - изменение размеров изображения
    image = pygame.transform.scale(load_image("images/enemy.png"), (90, 90))

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.enemy_hitbox = pygame.rect.Rect(self.x, self.y, 90, 90)
        self.enemy_color = pygame.color.Color((127, 0, 255))

        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = Enemy.image
        self.sprite.rect = self.enemy_hitbox
        self._ = pygame.sprite.GroupSingle()
        self._.add(self.sprite)

    def draw(self, screen: pygame.Surface, is_show_hitbox=True):
        self._.draw(screen)
        if is_show_hitbox:
            pygame.draw.rect(screen, self.enemy_color, self.enemy_hitbox, width=2)

    def chase_player(self, player_pos_x, player_pos_y, tick):
        enemy_pos_x = self.enemy_hitbox.x + 45
        enemy_pos_y = self.enemy_hitbox.y + 45
        direction_x = (player_pos_x - enemy_pos_x) / abs(player_pos_x - enemy_pos_x) if player_pos_x - enemy_pos_x else 0
        direction_y = (player_pos_y - enemy_pos_y) / abs(player_pos_y - enemy_pos_y) if player_pos_y - enemy_pos_y else 0
        self.x += (Enemy.SPEED * direction_x * tick) / 1000
        self.y += (Enemy.SPEED * direction_y * tick) / 1000
        self.enemy_hitbox.x = self.x
        self.enemy_hitbox.y = self.y