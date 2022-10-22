import pygame

class Trail(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.timeOfLife = 20
        self.image = pygame.image.load('img/purple.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)

    def move(self, ship):
        self.rect = self.image.get_rect(center=(ship.posX,ship.posY + 44))

