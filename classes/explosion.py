import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos

        self.explosionFrame = 60
        self.explosionTick = 60

        self.frame = 1
        self.frames = []
        for counter in range(0,11):
            self.frames.append(pygame.image.load('img/explosion_frames/tile' + str(counter) + '.png').convert_alpha())

        self.image = self.frames[0]
        self.rect = self.frames[0].get_rect(center = pos)


    def update(self):
        
        if self.explosionFrame < 0:
            self.explosionFrame = 60
            if self.frame < 11:
                self.image = self.frames[self.frame]
                self.rect = self.frames[self.frame].get_rect(center = self.pos)
                self.frame += 1
                return False
            else:
                return True
        
        self.explosionFrame -= self.explosionTick
        return False

