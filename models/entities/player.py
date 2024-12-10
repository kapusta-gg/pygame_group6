import pygame


class Player:
    PLAYER_SPEED = 100
    DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
    KEYS_TO_IND = {pygame.K_w: UP,
                   pygame.K_a: LEFT,
                   pygame.K_d: RIGHT,
                   pygame.K_s: DOWN}
    which_direction = [False, False, False, False]

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.player_hitbox = pygame.rect.Rect(x, y, 90, 90)
        self.player_color = pygame.color.Color((0, 255, 0))

    def draw(self, screen: pygame.Surface, is_hitbox=True):
        if is_hitbox:
            pygame.draw.rect(screen, self.player_color, self.player_hitbox, width=2)

    def change_movement(self, key, is_press):
        ind = Player.KEYS_TO_IND[key]
        Player.which_direction[ind] = is_press
        x = sum(Player.DIRECTIONS[i][0] for i in range(4) if Player.which_direction[i])
        y = sum(Player.DIRECTIONS[i][1] for i in range(4) if Player.which_direction[i])
        self.move_x = x
        self.move_y = y

    def move(self, tick):
        self.x += (self.move_x * tick * Player.PLAYER_SPEED)
        self.y += (self.move_y * tick * Player.PLAYER_SPEED)
        self.player_hitbox = pygame.rect.Rect(int(self.x), int(self.y) , 90, 90)