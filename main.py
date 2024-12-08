import pygame

from models.map.rooms import Room
from models.interface.minimap import MiniMap
from models.interface.hud import HUD
from models.entities.player import Player
from models.entities.enemies import Enemy


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

    running = True
    while running:
        # Обрабатываем события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Отрисовка объектов

        room.draw(screen)
        map.draw(screen)
        hud.draw(screen)
        player.draw(screen)

        enemy.draw(screen)
        # Выполняем логику (пока пусто)
        # Обновление экрана
        pygame.display.flip()