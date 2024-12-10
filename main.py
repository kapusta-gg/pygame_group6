import pygame

from models.map.rooms import Room
from models.map.objects import *
from models.interface.minimap import MiniMap
from models.interface.hud import HUD
from models.entities.player import Player
from models.entities.enemies import *

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
KEYS_TO_IND = {pygame.K_w: UP,
               pygame.K_a: LEFT,
               pygame.K_d: RIGHT,
               pygame.K_s: DOWN}

def change_movement(ind, is_press, all_bool_movements):
    all_bool_movements[ind] = is_press
    x = sum(DIRECTIONS[i][0] for i in range(4) if all_bool_movements[i])
    y = sum(DIRECTIONS[i][1] for i in range(4) if all_bool_movements[i])
    return x, y

if __name__ == '__main__':
    pygame.init()
    size = w, h = 1000, 800
    screen = pygame.display.set_mode(size)

    room = Room()
    map = MiniMap()
    hud = HUD()

    player = Player(450, 350)

    # Тестовая
    enemy = Enemy(300, 300)
    objectt = Object(100, 100)

    pos = (0, 0)
    isShowHitbox = True
    isMovePlayer = [False, False, False, False]

    clock = pygame.time.Clock()

    running = True
    while running:
        tick = clock.tick()
        # Обрабатываем события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    isShowHitbox = not isShowHitbox
                # Проверка WASD
                [change_movement(KEYS_TO_IND[i], True, isMovePlayer)
                 for i in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d] if event.key == i]
                pos = change_movement(UP, isMovePlayer[UP], isMovePlayer)
            if event.type == pygame.KEYUP:
                # Проверка WASD
                [change_movement(KEYS_TO_IND[i], False, isMovePlayer)
                 for i in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d] if event.key == i]
                pos = change_movement(UP, isMovePlayer[UP], isMovePlayer)

        # Отрисовка объектов
        screen.fill((0, 0, 0))
        hud.draw(screen, is_hitbox=isShowHitbox)
        room.draw(screen, is_hitbox=isShowHitbox)
        map.draw(screen)
        player.draw(screen, is_hitbox=isShowHitbox)

        enemy.draw(screen, is_hitbox=isShowHitbox)
        objectt.draw(screen, is_hitbox=isShowHitbox)
        # Выполняем логику
        if any(isMovePlayer):
            player.move(*(i * tick / 1000 for i in pos))
        # Обновление экрана
        pygame.display.flip()