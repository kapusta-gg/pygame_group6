import pygame


class Room:
    def __init__(self):
        self.room = pygame.rect.Rect(50, 50, 900, 700)
        self.room_color = pygame.color.Color((0, 120, 255))
        self.field = Field()

        # Тестовая
        self.door = Door(400, 50)

    def draw(self, screen: pygame.Surface):
        self.field.draw(screen)
        pygame.draw.rect(screen, self.room_color, self.room, width=2)

        self.door.draw(screen)


class Door:
    def __init__(self, x: int, y: int):
        self.door = pygame.rect.Rect(x, y, 200, 50)
        self.door_color = pygame.color.Color((0, 255, 255))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.door_color, self.door, width=2)


class Field:
    def __init__(self):
        self.field_hitbox = pygame.rect.Rect(100, 100, 800, 600)
        self.field_color = pygame.color.Color((0, 0, 255))

    def draw(self, screen):
        pygame.draw.rect(screen, self.field_color, self.field_hitbox, width=2)
