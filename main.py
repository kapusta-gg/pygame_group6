from models.map.rooms import Room
from models.map.objects import *
from models.interface.minimap import MiniMap
from models.interface.hud import HUD
from models.entities.player import Player
from models.entities.enemies import *


if __name__ == '__main__':
    pygame.init()
    size = w, h = 1000, 800
    screen = pygame.display.set_mode(size)

    room = Room()
    map = MiniMap()
    hud = HUD()

    room.field.load_room("rooms_levels/room2.txt")

    player = Player(450, 350)

    isShowHitbox = True

    clock = pygame.time.Clock()

    running = True
    while running:
        tick = clock.tick()
        # Обрабатываем события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    isShowHitbox = not isShowHitbox
                if event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
                    player.change_movement(event.key, True)
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
                    player.change_movement(event.key, False)

        # Отрисовка объектов
        screen.fill((0, 0, 0))
        map.draw(screen)
        room.draw(screen, is_show_hitbox=isShowHitbox)
        hud.draw(screen, is_show_hitbox=isShowHitbox)
        player.draw(screen, is_show_hitbox=isShowHitbox)
        # Выполняем логику
        for col in room.field.field:
            for obj in col:
                if issubclass(Enemy, obj.__class__):
                    obj.chase_player(*player.get_coords(), tick)
        if any(player.which_direction):
            player.move(tick)
        # Обновление экрана
        pygame.display.flip()