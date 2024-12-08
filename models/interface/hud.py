import pygame


class HUD:
    def __init__(self):
        self.active_item = ActiveItemHUD()
        self.health = HealthHUD()
        self.items = ItemsHUD()

    def draw(self, screen: pygame.Surface):
        self.active_item.draw(screen)
        self.health.draw(screen)
        self.items.draw(screen)


class ActiveItemHUD:
    def __init__(self):
        self.item = pygame.rect.Rect(0, 0, 100, 100)
        self.item_color = pygame.color.Color((200, 200, 200))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.item_color, self.item, width=2)


class HealthHUD:
    FONT_SIZE = 30

    def __init__(self):
        self.item = pygame.rect.Rect(100, 0, 100, 50)
        self.item_color = pygame.color.Color((100, 100, 100))
        self.font = pygame.font.Font(None, HealthHUD.FONT_SIZE)
        self.health = 0
        self.text = self.font.render(str(self.health), True, (255, 255, 255))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.item_color, self.item, width=2)
        screen.blit(self.text, (140, 15))


class ItemsHUD:
    FONT_SIZE = 30

    def __init__(self):
        self.item = pygame.rect.Rect(0, 100, 100, 100)
        self.item_color = pygame.color.Color((150, 150, 150))

        self.font = pygame.font.Font(None, ItemsHUD.FONT_SIZE)
        self.items_num_list = [0, 0, 0]
        self.items_text_list = [self.font.render(str(i), True, (255, 255, 255)) for i in self.items_num_list]

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.item_color, self.item, width=2)
        for i in range(3):
            screen.blit(self.items_text_list[0], (self.item.x + 50, self.item.y + 10 + 30 * i))