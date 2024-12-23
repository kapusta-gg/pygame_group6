import pygame
from methods import load_image
from models.map.rooms import *


class Player:
    SPEED = 150
    DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
    KEYS_TO_IND = {pygame.K_w: UP,
                   pygame.K_s: DOWN,
                   pygame.K_a: LEFT,
                   pygame.K_d: RIGHT}
    which_direction = [False, False, False, False]
    image = load_image("images/player.png")

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.player_hitbox = pygame.rect.Rect(self.x, self.y, 80, 100)
        self.player_color = pygame.color.Color((0, 255, 0))

        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = Player.image
        self.sprite.rect = self.player_hitbox
        self._ = pygame.sprite.GroupSingle()
        self._.add(self.sprite)

    def change_movement(self, key: int, state: bool):
        ind = Player.KEYS_TO_IND[key]
        Player.which_direction[ind] = state
        x = sum([Player.DIRECTIONS[i][0] for i in range(4) if Player.which_direction[i]])
        y = sum([Player.DIRECTIONS[i][1] for i in range(4) if Player.which_direction[i]])
        self.direction_x = x
        self.direction_y = y

    def draw(self, screen: pygame.Surface, is_show_hitbox=True):
        self._.draw(screen)
        if is_show_hitbox:
            pygame.draw.rect(screen, self.player_color, self.player_hitbox, width=2)

    def move(self, tick: float, objs: list[Object]):
        move_x = (Player.SPEED * self.direction_x * tick) / 1000
        move_y = (Player.SPEED * self.direction_y * tick) / 1000
        x = self.x + move_x
        y = self.y + move_y

        if any(pygame.sprite.spritecollide(self.sprite, objs, False)):
            self.player_hitbox.x = x
            self.player_hitbox.y = y
            return
        if not 100 <= x <= 820 or not 100 <= y <= 600:
            return
        self.x = x
        self.y = y
        self.player_hitbox.x = self.x
        self.player_hitbox.y = self.y

    def get_coords(self):
        return self.player_hitbox.x + 45, self.player_hitbox.y + 45