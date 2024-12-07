import pygame


if __name__ == '__main__':
    pygame.init()
    size = w, h = 1000, 800
    screen = pygame.display.set_mode(size)

    running = True
    while running:
        # Обрабатываем события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Отрисовка объектов
        screen.fill((255, 0, 0))
        # Выполняем логику (пока пусто)
        # Обновление экрана
        pygame.display.flip()