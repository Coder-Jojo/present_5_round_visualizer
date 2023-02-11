import pygame
from sys import exit
import time
from sbox import Sbox


def run_gui(sbox_layers, lines, options):
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()


    # fill screen with red color
    screen.fill('#444444')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    options['next'] = True

        if options['stop']:
            break

        screen.blit(lines.surface, (0, 0))

        screen.blit(sbox_layers[0].surface, (30, 20))
        screen.blit(sbox_layers[1].surface, (30, 170))
        screen.blit(sbox_layers[2].surface, (30, 320))
        screen.blit(sbox_layers[3].surface, (30, 470))
        screen.blit(sbox_layers[4].surface, (30, 620))

        pygame.display.flip()
        clock.tick(32)




if __name__ == '__main__':
    run_gui()