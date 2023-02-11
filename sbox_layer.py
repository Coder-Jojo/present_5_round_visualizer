import pygame
from sbox import Sbox

class SboxLayer:
    def __init__(self):
        self.surface = pygame.Surface((40 * 16, 40))
        self.surface.set_colorkey((0, 0, 0))
        self.sboxes = []

        for i in range(0, 40 * 16, 40):
            sbox = Sbox()
            self.sboxes.append(sbox)
            self.surface.blit(sbox.surface, (i, 0))


    def activate(self, index):
        self.sboxes[index].activate()
        self.surface.blit(self.sboxes[index].surface, (index * 40, 0))

    
    def deactivate(self, index):
        self.sboxes[index].deactivate()
        self.surface.blit(self.sboxes[index].surface, (index * 40, 0))