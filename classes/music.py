import pygame

class Music():
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        pygame.mixer.music.load("path")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1, 0.0)

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()
