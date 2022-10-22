import pygame

class Star(pygame.sprite.Sprite):
    speed = 20

    def __init__(self, pos):
        super().__init__()
        # set rand image
        #self.image = starImage
        self.rect = self.image.get_rect(center=pos)
