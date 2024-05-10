import pygame.sprite

from button import Button
from player import Player
from object import Object
from constants import *

MAP = pygame.sprite.Group([Object((i * BLOCK_WIDTH, screen_h - BLOCK_HEIGHT)) for i in range(50)])
all_sprites = pygame.sprite.Group()
all_objects = pygame.sprite.Group()
player = Player()
all_sprites.add(MAP)
all_objects.add(MAP)
all_sprites.add(player)

main_surface = pygame.Surface((screen_w, screen_h))

class Game:
    def __init__(self):
        pass

    def __call__(self, keys, mouse_pos, mouse_k):
        screen.blit(main_surface, (0, 0))
        main_surface.fill(BLACK)

        scene = "GAME"
        if keys[pygame.K_q]:
            scene = "MENU"

        player.update(keys, all_objects)
        all_objects.update(player.get_camera_cords())
        all_sprites.draw(main_surface)

        return scene