import pygame

class Sbox:
    def __init__(self):
        self.surface = pygame.Surface((30, 30))
        self.surface.fill((255, 255, 0))

    def activate(self):
        # change color of surface
        self.surface.fill((100, 0, 0))

    def deactivate(self):
        self.surface.fill((255, 255, 0))
