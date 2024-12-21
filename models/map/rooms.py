import pygame.transform

from models.map.objects import *
from models.entities.enemies import *


class Room:
    def __init__(self):
        self.room = pygame.rect.Rect(50, 50, 900, 700)
        self.room_color = pygame.color.Color((0, 120, 255))
        self.field = Field()

        # Тестовая
        self.door = Door(425, 50)

    def draw(self, screen: pygame.Surface, is_show_hitbox=True):
        self.field.draw(screen, is_show_hitbox=is_show_hitbox)
        if is_show_hitbox:
            pygame.draw.rect(screen, self.room_color, self.room, width=2)

        self.door.draw(screen, is_show_hitbox=is_show_hitbox)


class Door:
    def __init__(self, x: int, y: int):
        self.door = pygame.rect.Rect(x, y, 150, 50)
        self.door_color = pygame.color.Color((0, 255, 255))

    def draw(self, screen: pygame.Surface, is_show_hitbox=True):
        if is_show_hitbox:
            pygame.draw.rect(screen, self.door_color, self.door, width=2)


class Field:
    CELL_SIZE = 100
    image = pygame.transform.scale(load_image("images/floor.png"), (800, 600))

    def __init__(self):
        self.field_hitbox = pygame.rect.Rect(100, 100, 800, 600)
        self.field_color = pygame.color.Color((0, 0, 255))
        self.field = [[None] * 8 for _ in range(6)]

        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = Field.image
        self.sprite.rect = self.field_hitbox
        self._ = pygame.sprite.GroupSingle()
        self._.add(self.sprite)

    def draw(self, screen: pygame.Surface, is_show_hitbox=True):
        self._.draw(screen)
        if is_show_hitbox:
            pygame.draw.rect(screen, self.field_color, self.field_hitbox, width=2)
        for i in range(8):
            for j in range(6):
                if self.field[j][i] is not None:
                    self.field[j][i].draw(screen, is_show_hitbox=is_show_hitbox)

    def load_room(self, room_txt):
        # файл с матрицей 8х6
        # 0 - земля
        # 1 - противник (объекта класса Enemy)
        # 2 - препятствие (объекта класса Object)
        f = open(room_txt, "r")
        l = f.readlines()
        f.close()
        for i in range(8):
            for j in range(6):
                if l[j][i] == "1":
                    self.field[j][i] = Rock(100 + i * Field.CELL_SIZE, 100 + j * Field.CELL_SIZE)
                elif l[j][i] == "2":
                    self.field[j][i] = Enemy(100 + i * Field.CELL_SIZE, 100 + j * Field.CELL_SIZE)
