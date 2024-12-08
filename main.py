import pygame

from models.map.rooms import Room
from models.interface.minimap import MiniMap
from models.interface.hud import HUD

if __name__ == '__main__':
    pygame.init()
    size = w, h = 1000, 800
    screen = pygame.display.set_mode(size)

    room = Room()
    map = MiniMap()
    hud = HUD()

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
        # Выполняем логику (пока пусто)
        # Обновление экрана
        pygame.display.flip()