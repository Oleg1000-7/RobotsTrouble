from constants import *


class Object(pygame.sprite.Sprite):
    def __init__(self, cords):
        super().__init__()
        self.image = pygame.Surface((BLOCK_WIDTH, BLOCK_HEIGHT))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.center = cords
        self.x, self.y = cords
        self.hp = 40

    def damage(self):
        self.hp -= 20
        if self.hp <= 0:
            self.kill()

    def update(self, **kwargs):
        offset = kwargs["offset"]
        self.rect.x = self.x - offset[0]
        self.rect.y = self.y - offset[1]
