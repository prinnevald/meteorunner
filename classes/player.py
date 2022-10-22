import pygame
from classes.trail import Trail
from classes.bullet import Bullet

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, group):

        # init and variables
        super().__init__()
        self.posX = pos[0]
        self.posY = pos[1]
        self.speed = 10

        self.health = 100

        self.reload = 100
        self.attackSpeed = 3
        self.autofire = False

        # so that we can add elements like Trail
        self.trail = Trail((self.posX, self.posY + 44))
        self.group = group
        self.group.add(self.trail)

        # loading up player image (spaceship)
        self.image = pygame.image.load('img/player.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)


    # ship movement
    def move(self, to):
        self.posX += to
        self.update()


    # tick to check if reload
    def reloadTick(self):
        if self.reload > 0:
            self.reload -= self.attackSpeed
        elif self.reload < 0:
            self.reload = 0


    # shoot and reset reload 
    def shoot(self):
        self.reload = 100
        return Bullet((self.posX, self.posY))

    def getPosition(self):
        return (self.posX, self.posY)

    def getWidth(self):
        return self.image.get_width()


    # autofire functions
    def isAutofire(self):
        return self.autofire

    def setAutofire(self):
        self.autofire = not self.autofire


    # return if ready to fire
    def ready(self):
        return self.reload == 0


    # update
    def update(self):
        self.rect = self.image.get_rect(center = (self.posX, self.posY))        
        self.trail.move(self)

