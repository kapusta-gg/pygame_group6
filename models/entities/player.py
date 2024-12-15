import pygame


class Player:
    SPEED = 150
    DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
    KEYS_TO_IND = {pygame.K_w: UP,
                   pygame.K_s: DOWN,
                   pygame.K_a: LEFT,
                   pygame.K_d: RIGHT}
    which_direction = [False, False, False, False]

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.player_hitbox = pygame.rect.Rect(self.x, self.y, 90, 90)
        self.player_color = pygame.color.Color((0, 255, 0))

    def change_movement(self, key: int, state: bool):
        ind = Player.KEYS_TO_IND[key]
        Player.which_direction[ind] = state
        x = sum([Player.DIRECTIONS[i][0] for i in range(4) if Player.which_direction[i]])
        y = sum([Player.DIRECTIONS[i][1] for i in range(4) if Player.which_direction[i]])
        self.direction_x = x
        self.direction_y = y

    def draw(self, screen: pygame.Surface, is_show_hitbox=True):
        if is_show_hitbox:
            pygame.draw.rect(screen, self.player_color, self.player_hitbox, width=2)

    def move(self, tick: float):
        self.x += (Player.SPEED * self.direction_x * tick) / 1000
        self.y += (Player.SPEED * self.direction_y * tick) / 1000
        self.player_hitbox.x = self.x
        self.player_hitbox.y = self.y