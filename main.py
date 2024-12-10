import pygame

from models.map.rooms import Room
from models.map.objects import *
from models.interface.minimap import MiniMap
from models.interface.hud import HUD
from models.entities.player import Player
from models.entities.enemies import *

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

def func(x):
    if x < -1:
        return -1
    if x > 1:
        return 1
    return x

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
                if event.key == pygame.K_w:
                    direction = (0, -1)
                    isMovePlayer = True
                if event.key == pygame.K_a:
                    direction = (-1, 0)
                    isMovePlayer = True
                if event.key == pygame.K_s:
                    direction = (0, 1)
                    isMovePlayer = True
                if event.key == pygame.K_d:
                    direction = (1, 0)
                    isMovePlayer = True
                if isMovePlayer:
                    pos = (func(pos[0] + direction[0]), func(pos[1] + direction[1]))
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_a or \
                    event.key == pygame.K_s or event.key == pygame.K_d:
                    isMovePlayer = False
        # Отрисовка объектов
        screen.fill((0, 0, 0))
        hud.draw(screen, is_hitbox=isShowHitbox)
        room.draw(screen, is_hitbox=isShowHitbox)
        map.draw(screen)
        player.draw(screen, is_hitbox=isShowHitbox)

        enemy.draw(screen, is_hitbox=isShowHitbox)
        objectt.draw(screen, is_hitbox=isShowHitbox)
        # Выполняем логику (пока пусто)
        if isMovePlayer:
            player.move(*(i * tick / 1000 for i in pos))
        # Обновление экрана
        pygame.display.flip()