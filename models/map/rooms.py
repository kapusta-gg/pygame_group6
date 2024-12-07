import pygame


class Room:
    def __init__(self):
        self.room = pygame.rect.Rect(50, 50, 900, 700)
        self.room_color = pygame.color.Color((0, 120, 255))
        self.field = Field()

    def draw(self, screen: pygame.Surface):
        self.field.draw(screen)
        pygame.draw.rect(screen, self.room_color, self.room, width=2)


class Door: # Пока не трогаем
    pass


class Field:
    def __init__(self):
        self.field_hitbox = pygame.rect.Rect(100, 100, 800, 600)
        self.field_color = pygame.color.Color((0, 0, 255))

        self.font = pygame.font.Font(None, 25)
        self.text = self.font.render("Поле", True, (0, 0, 255))

    def draw(self, screen):
        pygame.draw.rect(screen, self.field_color, self.field_hitbox, width=2)

        #Отрисовка текста
        screen.blit(self.text, (500, 400))