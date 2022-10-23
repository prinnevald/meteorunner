import pygame
from classes.explosion import Explosion

class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.speed = 10
        self.posX = pos[0]
        self.posY = pos[1]

        self.image = pygame.image.load('img/yellow.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (16,32))
        self.rect = self.image.get_rect(center=pos)

        self.sound = pygame.mixer.Sound('sfx/laser.ogg')
        self.sound.set_volume(0.5)
        self.sound.play()


    def move(self):
        if self.posY > 0:
            self.posY -= self.speed
            self.update()
            return False
        return True


    def explode(self):
        return Explosion((self.posX, self.posY))


    def update(self):
        self.rect = self.image.get_rect(center=(self.posX, self.posY))
