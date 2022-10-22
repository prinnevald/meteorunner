import pygame
from random import randint

class Meteor(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.speed = 5
        self.posX = pos[0]
        self.posY = pos[1]
        # self.angle = randint(0, 360)
        # self.angularSpeed = randint(-45,45)

        self.image = pygame.image.load('img/meteor' + str(randint(1, 3)) + '.png').convert_alpha()
        # self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(center = pos)


    def move(self):
        # self.angle += self.angularSpeed
        self.posY += self.speed
        self.update()


    def getWidth(self):
        return self.image.get_width()


    def getPosition(self):
        return self.posY

    
    def update(self):
        self.rect = self.image.get_rect(center = (self.posX, self.posY))
